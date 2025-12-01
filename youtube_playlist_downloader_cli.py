import os
import shutil
import platform
import subprocess
import yt_dlp
import time
import logging
import re
from urllib.parse import urlparse
from errors import interpretar_erro

SO = platform.system()  # Windows, Linux, Darwin (macOS)

# =====================================================
#        CONFIGURAR SISTEMA DE LOGS
# =====================================================

LOG_FILE = "youtube_downloader.log"

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler(LOG_FILE),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger(__name__)


# =====================================================
#        VERIFICADOR DE DEPENDÊNCIAS DO SISTEMA
# =====================================================

def verificar_dependencias():
    erros = []

    # 1️⃣ Verificar FFmpeg
    if shutil.which("ffmpeg") is None:
        erros.append("ffmpeg")

    if erros:
        print("\n❌ Detectamos dependências faltando:")
        for err in erros:
            print(f"   - {err}")

        print("\n⚠️ Siga as instruções abaixo para instalar:")

        if "ffmpeg" in erros:
            print("\n📌 Como instalar o FFmpeg:")

            if SO == "Windows":
                print("""
➡ WINDOWS:
1. Baixe o FFmpeg:
   https://www.gyan.dev/ffmpeg/builds/

2. Extraia em C:\\ffmpeg

3. Adicione ao PATH:
   - Abra "Editar variáveis de ambiente"
   - Edite "Path"
   - Adicione:
     C:\\ffmpeg\\bin
                """)

            elif SO == "Linux":
                print("""
➡ LINUX (Ubuntu/Debian):
sudo apt update
sudo apt install ffmpeg

➡ LINUX (Arch):
sudo pacman -S ffmpeg
                """)

            elif SO == "Darwin":
                print("""
➡ macOS:
brew install ffmpeg
                """)

        print("\nDepois de instalar, execute o programa novamente.\n")
        exit(1)

    return True


# =====================================================
#        OUTRAS FUNÇÕES DO SEU SCRIPT
# =====================================================

def clear():
    os.system("cls" if SO == "Windows" else "clear")


def validar_url_youtube(url):
    """Valida se a URL é uma URL válida do YouTube"""
    try:
        parsed = urlparse(url)
        
        # Verificar domínio
        if "youtube.com" not in parsed.netloc and "youtu.be" not in parsed.netloc:
            return False
        
        # Verificar se contém parâmetro de playlist
        if "youtube.com" in parsed.netloc:
            if "list=" not in url:
                return False
        
        return True
    except Exception as e:
        logger.error(f"Erro ao validar URL: {e}")
        return False


def validar_playlist(url):
    try:
        logger.info(f"Validando playlist: {url}")
        ydl_opts = {"quiet": True, "extract_flat": True, "skip_download": True}
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=False)

        if "entries" not in info or len(info["entries"]) == 0:
            logger.warning("Playlist não contém vídeos públicos")
            return False, 0

        total_publicos = sum(1 for item in info["entries"] if item)
        logger.info(f"Playlist validada com sucesso. Total de vídeos: {total_publicos}")
        return True, total_publicos

    except yt_dlp.utils.DownloadError as e:
        logger.error(f"Erro de download: {e}")
        return False, 0
    except Exception as e:
        logger.error(f"Erro ao validar playlist: {e}")
        return False, 0


# =====================================================
#  👉 SISTEMA DE DOWNLOAD COM TRATAMENTO DE ERROS AMIGÁVEIS
# =====================================================

def baixar_playlist(url, pasta_destino, gerar_mp3=False):

    def hook(d):
        print_progress(d)

    # Capturar avisos e erros brutos
    def my_logger(msg):
        msg = msg.strip()
        if msg.startswith("ERROR:") or "WARNING" in msg:
            mensagem_amigavel = interpretar_erro(msg)
            logger.warning(f"YouTube: {mensagem_amigavel}")
            print(f"\n❗ {mensagem_amigavel}")

    ydl_opts_video = {
        "format": "bestvideo+bestaudio/best",
        "merge_output_format": "mp4",
        "outtmpl": os.path.join(pasta_destino, "%(title)s.%(ext)s"),
        "noplaylist": False,
        "logger": type("L", (), {"debug": lambda s: None,
                                 "info": lambda s: None,
                                 "warning": my_logger,
                                 "error": my_logger}),
        "progress_hooks": [hook],
    }

    logger.info(f"Iniciando download da playlist: {url}")
    logger.info(f"Destino: {pasta_destino}")
    print("\n📥 Baixando vídeos (MP4)...\n")

    try:
        with yt_dlp.YoutubeDL(ydl_opts_video) as ydl:
            ydl.download([url])
        logger.info("Download MP4 concluído com sucesso")

    except yt_dlp.utils.DownloadError as e:
        logger.error(f"Erro de download: {e}")
        print("\n❌ Erro durante o download:")
        print("➡", interpretar_erro(str(e)))
        return
    except Exception as erro:
        logger.error(f"Erro inesperado durante download: {erro}")
        print("\n❌ Erro durante o download:")
        print("➡", interpretar_erro(str(erro)))
        return

    # ================================
    # EXTRAIR MP3
    # ================================
    if gerar_mp3:
        logger.info("Iniciando extração de áudio MP3")
        print("\n🎧 Extraindo áudio (MP3)...\n")

        for arquivo in os.listdir(pasta_destino):
            if arquivo.lower().endswith(".mp4"):
                caminho_mp4 = os.path.join(pasta_destino, arquivo)
                nome = os.path.splitext(arquivo)[0]
                caminho_mp3 = os.path.join(pasta_destino, nome + ".mp3")

                ydl_opts_mp3 = {
                    "format": "bestaudio/best",
                    "outtmpl": caminho_mp3,
                    "quiet": True,
                    "postprocessors": [
                        {
                            "key": "FFmpegExtractAudio",
                            "preferredcodec": "mp3",
                            "preferredquality": "192",
                        }
                    ],
                }

                try:
                    with yt_dlp.YoutubeDL(ydl_opts_mp3) as ydl:
                        ydl.download([caminho_mp4])
                    logger.info(f"MP3 extraído com sucesso: {caminho_mp3}")
                    print(f"✅ MP3 extraído: {nome}.mp3")

                except Exception as erro:
                    logger.error(f"Erro ao converter '{arquivo}' para MP3: {erro}")
                    print(f"\n❌ Erro ao converter '{arquivo}' para MP3:")
                    print("➡", interpretar_erro(str(erro)))



# =====================================================
#        SISTEMA DE PROGRESSO
# =====================================================

def print_progress(d):
    if d['status'] == 'downloading':
        tamanho = d.get('total_bytes') or d.get('total_bytes_estimate')
        baixado = d.get('downloaded_bytes', 0)
        if tamanho:
            pct = baixado / tamanho * 100
            print(f"\rBaixando → {pct:.1f}%", end='')

    elif d['status'] == 'finished':
        print(f"\r✅ Concluído: {d['filename']}                    ")


# =====================================================
#                     MENU PRINCIPAL
# =====================================================

def menu():

    verificar_dependencias()

    while True:
        clear()
        print("==============================================")
        print("      🎬 YOUTUBE PLAYLIST DOWNLOADER CLI")
        print("==============================================")
        print("1️⃣  Baixar uma playlist")
        print("2️⃣  Sair")
        print("==============================================")

        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            logger.info("Usuário iniciou novo download")
            url = input("\n👉 Cole aqui a URL da playlist: ").strip()
            
            # Validar URL
            if not url:
                print("❌ URL não pode estar vazia!")
                logger.warning("URL vazia fornecida")
                input("\nENTER para continuar...")
                continue
            
            if not validar_url_youtube(url):
                print("❌ URL inválida! Certifique-se que é uma playlist do YouTube.")
                logger.warning(f"URL inválida fornecida: {url}")
                input("\nENTER para continuar...")
                continue
            
            print("\n🔎 Verificando playlist, aguarde...\n")
            ok, total = validar_playlist(url)

            if not ok:
                print("❌ Playlist inválida ou sem vídeos públicos.")
                logger.warning("Playlist inválida ou sem vídeos")
                input("\nENTER para continuar...")
                continue

            print(f"✅ Playlist válida! Vídeos públicos: {total}")

            pasta = input("\n📁 Pasta de destino:\n→ ").strip()
            
            if not pasta:
                print("❌ Pasta não pode estar vazia!")
                logger.warning("Pasta vazia fornecida")
                input("\nENTER para continuar...")
                continue
            
            # Criar pasta se não existir
            if not os.path.isdir(pasta):
                try:
                    os.makedirs(pasta, exist_ok=True)
                    print(f"📁 Pasta criada: {pasta}")
                    logger.info(f"Pasta criada automaticamente: {pasta}")
                except Exception as e:
                    print(f"\n❌ Erro ao criar pasta: {e}")
                    logger.error(f"Erro ao criar pasta {pasta}: {e}")
                    input("\nENTER para continuar...")
                    continue

            gerar_mp3 = input("\nExtrair MP3 também? (s/n) → ").strip().lower() == "s"
            logger.info(f"Opção MP3: {'Sim' if gerar_mp3 else 'Não'}")

            print("\n📥 Iniciando download...\n")

            baixar_playlist(url, pasta, gerar_mp3)

            print("\n🎉 Finalizado!")
            logger.info("Download finalizado com sucesso")
            input("\nENTER para voltar ao menu...")

        elif opcao == "2":
            print("\n👋 Saindo...")
            logger.info("Aplicação encerrada pelo usuário")
            time.sleep(1)
            break

        else:
            print("\n❌ Opção inválida!")
            logger.warning("Opção inválida fornecida")
            time.sleep(1)



if __name__ == "__main__":
    menu()
