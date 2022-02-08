# Funções do programa.

from exif import Image


def getDateImage(image):
    image = Image(image)
    if image.has_exif:
        property_1 = image.get("datetime_original")
        property_2 = image.get("datetime_digitized")
        property_3 = image.get("datetime")

        return {"data_original": property_1[0:10].replace(":", "/"),
                "data_digitalizada": property_2[0:10].replace(":", "/"),
                "data_modificada": property_3[0:10].replace(":", "/")}

    else:
        return None


def getFileType(file):
    file_type = file[file.find("."):len(file)].lower()
    if file_type in [".jpeg", ".gif", ".png", ".tiff", ".bmp", ".jpg"]:
        classe = "imagem"

    elif file_type in [".aac", ".mp3", ".wav", ".wma", ".dolby®", ".digital", ".dts"]:
        classe = "música"

    elif file_type in [".mpeg-1", ".mpeg-2", ".mpeg-4", ".avi", ".mov", ".avchd", ".mkv", ".mp4"]:
        classe = "vídeo"

    else:
        classe = "outro"

    return {"tipo": file_type, "classe": classe}
