# Funções do programa

import os


def getFileType(file):
    _, extension = os.path.splitext(file)
    extension = extension.lower()
    if extension in [".jpeg", ".gif", ".png", ".tiff", ".bmp", ".jpg"]:
        classe = "Imagem"

    elif extension in [".aac", ".mp3", ".wav", ".wma", ".dolby®", ".digital", ".dts"]:
        classe = "Música"

    elif extension in [".mpeg-1", ".mpeg-2", ".mpeg-4", ".avi", ".mov", ".avchd", ".mkv", ".mp4", ".3gp"]:
        classe = "Vídeo"

    elif extension in [".txt", ".doc", ".ppt", ".xls", ".pdf"]:
        classe = "Documento"

    elif extension in [".zip", ".rar", ".arj"]:
        classe = "Compacto"

    elif extension == ".exe":
        classe = "Executável"

    else:
        classe = None

    return {"tipo": extension, "classe": classe}
