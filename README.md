# 🎬 YouTube Playlist Downloader CLI

Um utilitário profissional, rápido e intuitivo para fazer download de playlists completas do YouTube diretamente para seu computador. Disponível para **Windows** e **Linux**.

---

## 📋 Sumário

- [Características](#-características)
- [Requisitos do Sistema](#-requisitos-do-sistema)
- [Instalação](#-instalação)
- [Como Usar](#-como-usar)
- [Tratamento de Erros](#-tratamento-de-erros)
- [Tecnologias](#-tecnologias-utilizadas)
- [Segurança](#-segurança--confiabilidade)
- [Estrutura do Projeto](#-estrutura-do-projeto)
- [Licença](#-licença)
- [Contato](#-contato)

---

## 🚀 Características

✅ **Download Completo** – Baixe playlists inteiras automaticamente com um único comando  
✅ **Múltiplos Formatos** – Suporte a MP4 com opção de extração de áudio em MP3  
✅ **Tratamento Inteligente de Erros** – Sistema robusto de interpretação e resolução de problemas  
✅ **Validação Automática** – Verifica a validade da playlist antes de iniciar o download  
✅ **Interface CLI Limpa** – Menu interativo e intuitivo, sem configurações complexas  
✅ **Barra de Progresso** – Acompanhamento visual do progresso do download  
✅ **Zero Dependências Externas** – Tudo está incluído no executável compilado  

---

## 💻 Requisitos do Sistema

| Recurso | Especificação |
|---------|---------------|
| **Conexão** | Internet ativa e estável |
| **Sistema Operacional** | Windows 10/11 (64-bit) ou Linux (Ubuntu/Debian/etc) |
| **Espaço em Disco** | Conforme tamanho da playlist |
| **Python** | ❌ **NÃO necessário** – Executável é self-contained |

---

## 📥 Instalação

### Windows

1. Baixe o arquivo `youtube-downloader.exe` mais recente
2. Coloque em uma pasta de sua escolha
3. Execute com duplo clique ou pelo terminal:
```bash
.\youtube-downloader.exe
```

### Linux

1. Baixe o arquivo `youtube-downloader`
2. Conceda permissão de execução:
```bash
chmod +x youtube-downloader
```
3. Execute:
```bash
./youtube-downloader
```

---

## 🎮 Como Usar

O programa funciona de forma totalmente interativa:

1. **Inicie o programa** executando o binário apropriado para seu SO
2. **Menu Principal** – Escolha a opção "1" para fazer download
3. **Cole a URL** – Insira o link da playlist do YouTube
4. **Validação** – O programa verifica a playlist automaticamente
5. **Selecione Destino** – Indique a pasta onde salvar os arquivos
6. **Opção MP3** – Defina se deseja extrair áudio em MP3
7. **Download** – O programa iniciará automaticamente o download

### Exemplo de Fluxo

```
==============================================
      🎬 YOUTUBE PLAYLIST DOWNLOADER CLI
==============================================
1️⃣  Baixar uma playlist
2️⃣  Sair
==============================================
Escolha uma opção: 1

👉 Cole aqui a URL da playlist: https://www.youtube.com/playlist?list=PLxxxxxxx

🔎 Verificando playlist, aguarde...
✅ Playlist válida! Vídeos públicos: 15

📁 Pasta de destino:
→ /home/usuario/Downloads/minhas-playlists

Extrair MP3 também? (s/n) → s

📥 Iniciando download...
```

---

## ⚠️ Tratamento de Erros

O programa identifica automaticamente problemas comuns e fornece mensagens claras:

| Erro | Mensagem |
|------|----------|
| Vídeo bloqueado por direitos autorais | "Este vídeo está bloqueado no seu país por direitos autorais" |
| Vídeo privado | "Este vídeo é privado e não pode ser baixado" |
| Vídeo removido | "O vídeo foi removido do YouTube e não está mais disponível" |
| Restrição de idade | "Este vídeo é restrito por idade e não pode ser baixado" |
| Falha de conexão | "Houve falha de conexão com o YouTube. Verifique sua internet" |
| Vídeos indisponíveis | "Alguns vídeos da playlist estão indisponíveis, mas os outros serão baixados" |

---

## 🧩 Tecnologias Utilizadas

| Componente | Descrição |
|-----------|-----------|
| **Python 3** | Linguagem base para o desenvolvimento |
| **yt-dlp** | Motor de download rápido e confiável para YouTube |
| **FFmpeg** | Processamento e conversão de áudio/vídeo |
| **PyInstaller** | Compilação para executável standalone |
| **Sistema de Erros** | Framework customizado de tratamento de exceções |

### Bibliotecas Python

```
yt-dlp          # YouTube Download
```

---

## 🛡️ Segurança & Confiabilidade

✔️ **Executável Compilado** – Código-fonte não exposto no binário  
✔️ **Sem Adware/Spyware** – Código 100% limpo e sem elementos maliciosos  
✔️ **Bibliotecas Oficiais** – Usa apenas repositórios confiáveis e verificados  
✔️ **Sem Coleta de Dados** – Sua privacidade é respeitada – nenhum dado é coletado  
✔️ **Open Source (Repositório Privado)** – Código revisável apenas pelos maintainers  
✔️ **Testado Antes de Release** – Cada versão passa por testes rigorosos  

---

## 📂 Estrutura do Projeto

```
youtube-download/
├── youtube_playlist_downloader_cli.py    # Script principal
├── errors.py                             # Sistema de tratamento de erros
├── youtube_playlist_downloader_cli.spec  # Configuração PyInstaller
├── build/                                # Arquivos compilados (gerados)
├── README.md                             # Este arquivo
└── .gitignore                            # (recomendado)
```

---

## 🔧 Desenvolvimento

### Requisitos para Desenvolvedores

```bash
python3 >= 3.8
pip install yt-dlp
```

### Compilar para Executável

```bash
pip install pyinstaller
pyinstaller youtube_playlist_downloader_cli.spec
```

O executável será gerado em `dist/youtube-downloader`

---

## 🧾 Licença

Este software é **proprietário** e distribuído sob licença restrita:

- ✅ Uso pessoal permitido
- ✅ Estudo e análise interna permitida
- ❌ Redistribuição proibida
- ❌ Modificação e relicenciamento proibidos
- ❌ Uso comercial proibido

**Todos os direitos reservados.**

---

## 🤝 Contato & Suporte

### Reportar Problemas

Se encontrar um bug ou comportamento inesperado:

1. Teste com a versão mais recente
2. Descreva o problema com detalhes (SO, URL, erro exato)
3. Abra uma **Issue** neste repositório com as informações

### Recursos

- **GitHub Issues** – Para reportar bugs e solicitar features
- **Documentação** – Verifique os exemplos de uso acima

---

## 📊 Status do Projeto

| Aspecto | Status |
|--------|--------|
| Funcionalidade | ✅ Completa |
| Windows (64-bit) | ✅ Estável |
| Linux | ✅ Estável |
| macOS | 🔶 Experimental |
| Manutenção | ✅ Ativa |

---

## 📝 Notas Importantes

- **Respeite os Direitos Autorais** – Use esta ferramenta apenas com conteúdo que você tem permissão para baixar
- **Termos de Serviço do YouTube** – Certifique-se de estar de acordo com a política de uso
- **Conexão Estável** – Recomenda-se uma conexão rápida para evitar interrupções
- **Espaço em Disco** – Playlists grandes podem consumir bastante espaço

---

**Desenvolvido com ❤️ e Python 3**

Última atualização: Dezembro de 2025