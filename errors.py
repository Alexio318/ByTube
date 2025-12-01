def interpretar_erro(erro: str) -> str:
    erro_low = erro.lower()

    if "copyright grounds" in erro_low or "blocked" in erro_low:
        return "Este vídeo está bloqueado no seu país por direitos autorais."

    if "private video" in erro_low:
        return "Este vídeo é privado e não pode ser baixado."

    if "video unavailable" in erro_low and "removed" in erro_low:
        return "O vídeo foi removido do YouTube e não está mais disponível."

    if "age-restricted" in erro_low:
        return "Este vídeo é restrito por idade e não pode ser baixado."

    if "no supported javascript runtime" in erro_low:
        return "Falta um JavaScript Runtime. O download pode funcionar, mas talvez com perda de qualidade."

    if "unable to download webpage" in erro_low or ("http" in erro_low and "error" in erro_low):
        return "Houve falha de conexão com o YouTube. Verifique sua internet."

    if "unavailable videos" in erro_low:
        return "Alguns vídeos da playlist estão indisponíveis, mas os outros serão baixados normalmente."

    return "Ocorreu um erro inesperado durante o download."
