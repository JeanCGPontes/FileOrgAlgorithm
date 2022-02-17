# FileOrgAlgorithm — Algoritmo de Organização de Arquivos

import os
import shutil
import sys

import functions

print(r"""
                 .__________________.
   .____________/  FileOrgAlgorithm  \____________.
  /                                                \
 /       Algoritmo de Organização de Arquivos       \
:                                                    :
|       CMD: python main.py diretório_da_pasta       |
:____________________________________________________:
""")

try:
    path = sys.argv[1]
    folders, images, videos, music, documents, compact, executable = 0, 0, 0, 0, 0, 0, 0

    for file in os.listdir(path):
        file_directory = fr"{path}\{file}"
        file_type = functions.getFileType(file_directory)["classe"]

        if file_type is None:
            continue

        if not os.path.exists(fr"{path}\{file_type}"):
            os.makedirs(fr"{path}\{file_type}")
            print(fr"Criado -+> {file_type}")
            shutil.move(src=file_directory, dst=fr"{path}\{file_type}\{file}")
            print(fr"Transferido {file} -+> {file_type}")

        else:
            shutil.move(src=file_directory, dst=fr"{path}\{file_type}\{file}")
            print(fr"Transferido {file} -+> {file_type}")

    print("""
    *******************************
    Processo finalizado com sucesso!
    *******************************
    """)


except IndexError:
    print("Erro: Falta o diretório da pasta!")
