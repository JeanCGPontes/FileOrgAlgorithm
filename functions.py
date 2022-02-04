# Funções do programa.

from exif import Image


def getDateImage(image):
    property_1 = Image(image).get("datetime_original")
    property_2 = Image(image).get("datetime_digitized")
    return [property_1[0:10].replace(":", "/"), property_2[0:10].replace(":", "/")]



