# FileOrgAlgorithm — Algoritmo de Organização de Arquivos

import os
import shutil
import sys

import functions

print(r"""
    ¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨
    FileOrgAlgorithm
    ¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨""")

try:
    path = sys.argv[1]
    folders, images, videos, music, documents, compact, executable = 0, 0, 0, 0, 0, 0, 0

    for file in os.listdir(path):
        file_directory = fr"{path}\{file}"
        file_type = functions.getFileType(file_directory)["classe"]

        if file_type is None:
            continue

        elif file_type == "Imagem":
            images += 1

        elif file_type == "Música":
            music += 1

        elif file_type == "Vídeo":
            videos += 1

        elif file_type == "Documento":
            documents += 1

        elif file_type == "Compacto":
            compact += 1

        elif file_type == "Executável":
            executable += 1

        if not os.path.exists(fr"{path}\{file_type}"):
            os.makedirs(fr"{path}\{file_type}")
            folders += 1
            print(fr"Criado -+> {file_type}")
            shutil.move(src=file_directory, dst=fr"{path}\{file_type}\{file}")
            print(fr"Transferido {file} -+> {file_type}")

        else:
            shutil.move(src=file_directory, dst=fr"{path}\{file_type}\{file}")
            print(fr"Transferido {file} -+> {file_type}")

    print(f"""
    ¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨
    Processo finalizado com sucesso!
    Transferidos:
        >{images} Imagens;
        >{videos} Vídeos;
        >{music} Músicas;
        >{documents} Documentos;
        >{compact} Compactos;
        >{executable} Executável.
    Criado {folders} pastas.
    ¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨""")

except IndexError:
    print("Erro: Falta o diretório da pasta!")
