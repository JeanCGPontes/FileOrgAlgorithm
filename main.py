# Será usado para este programa o paradigma procedural.
# SoftOrgDocuments — Software de Organização de Documentos.

import functions
import os

path = r"C:\Users\jeane\OneDrive\Imagens\Fotos do Computador da Thalia"

for a in range(0, len(os.listdir(path))):
    image_directory = fr"{path}\{os.listdir(path)[a]}"
    "print(functions.getDateImage(image_directory))"
    print(functions.getFileType(image_directory))
