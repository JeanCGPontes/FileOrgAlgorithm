# Será usado para este programa o paradigma procedural.
# SoftOrgDocuments — Software de Organização de Documentos.

import functions
import os

path = r"E:\Programação\Python\Projetos\SoftOrgDocuments\arquivo_com_fotos"

for a in range(0, len(os.listdir(path))):
    image_directory = fr"{path}\{os.listdir(path)[a]}"
    print(functions.getDateImage(image_directory))


"""for file in os.listdir(path):
    print(functions.getDateImage(fr"{path}\{file}"))"""



"""for directory, folders, files in os.walk(folder):
    for file in files:
        image_directory = os.path.join(os.path.realpath(directory), file)
        print(functions.getDateImage(image_directory))"""
