# Funções do programa.

from exif import Image


def getDateImage(image):
    property_1 = Image(image).datetime_original
    property_2 = Image(image).datetime_digitized
    property_3 = Image(image).datetime
    return [property_1[0:10].replace(":", "/"), property_2[0:10].replace(":", "/"), property_3[0:10].replace(":", "/")]
