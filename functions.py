# Funções do programa.
import os

from exif import Image


def getDateImage(image):
    image = Image(image)
    if image.has_exif:
        property_1 = image.get("datetime_original")
        property_2 = image.get("datetime_digitized")
        property_3 = image.get("datetime")

        return {"data_original": formatDate(property_1),
                "data_digitalizada": formatDate(property_2),
                "data_modificada": formatDate(property_3)}

    else:
        return {"data_original": "not found!",
                "data_digitalizada": "not found!",
                "data_modificada": "not found!"}


def getFileType(file):
    file_type = file[file.find("."):len(file)].lower()
    if file_type in [".jpeg", ".gif", ".png", ".tiff", ".bmp", ".jpg"]:
        classe = "Imagem"

    elif file_type in [".aac", ".mp3", ".wav", ".wma", ".dolby®", ".digital", ".dts"]:
        classe = "Música"

    elif file_type in [".mpeg-1", ".mpeg-2", ".mpeg-4", ".avi", ".mov", ".avchd", ".mkv", ".mp4", ".3gp"]:
        classe = "Vídeo"

    else:
        classe = None

    return {"tipo": file_type, "classe": classe}


def formatDate(datetime):
    try:
        return datetime[0:10].replace(":", "/")

    except TypeError:
        return "not found!"


def getFolders(path):
    directory_list = []
    list_folder_names = []
    for directory, folders, _ in os.walk(path):
        for folder in folders:
            directory_list.append(os.path.join(directory, folder).replace("\\", "/"))
            list_folder_names.append(folder)

    return {"nomes": list_folder_names, "diretorios": directory_list}
