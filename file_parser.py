from typing import Dict, List
import os
import shutil
from normalize import normalize


ARCHIVES = "archives"
UNKNOWN = "unknowns"

CATEGORIES: Dict[str, List] = {
    "images": ['jpeg', 'png', 'jpg', 'svg'],
    "videos": ['avi', 'mp4', 'mov', 'mkv'],
    "documents": ['doc', 'docx', 'txt', 'pdf', 'xlsx', 'pptx'],
    "music": ['mp3', 'ogg', 'wav', 'amr'],
    "archives": ['zip', 'gz', 'tar'],
    "unknowns": [],
    }

sorted_files_list = []
extensions_set = set()
unknown_ext_set = set()


def define_category(file_path: str):
    global CATEGORIES
    extension = file_path.split(".")[-1]

    for category, category_extensions in CATEGORIES.items():
        if extension in category_extensions:
            extensions_set.add(extension)
            return category

    CATEGORIES[UNKNOWN].append(extension)
    unknown_ext_set.add(extension)
    return UNKNOWN


def unpack_archive(archive_src: str, destination_folder: str):
    shutil.unpack_archive(archive_src, destination_folder)


def move_to_category_folder(src: str, destination: str):
    category = define_category(src)
    destination_folder: str = os.path.join(destination, category)  # - /target/images

    if not os.path.exists(destination_folder):
        os.mkdir(destination_folder)

    if category == ARCHIVES:
        unpack_archive(src, destination_folder)
        return

    filename: str = os.path.split(src)[-1]
    new_filename = normalize(filename)
    destination_filepath = os.path.join(destination_folder, new_filename)  # target/images/zobrazenna.jpeg
    sorted_files_list.append(destination_filepath)
    shutil.move(src, destination_filepath)


# to work for is function !!!!  
def arrange_files_sorting_in_folder(target_path: str, destination_folder: str = None):
    if destination_folder is None:
        destination_folder = target_path

    inner_files = os.listdir(target_path)
    for filename in inner_files:
        file_path: str = os.path.join(target_path, filename)

        if os.path.isdir(file_path):
            arrange_files_sorting_in_folder(file_path)

        elif os.path.isfile(file_path):
            move_to_category_folder(file_path, destination_folder)

        else:
            raise OSError
        
    # return target_path


"""old version"""
# import sys
# from pathlib import Path

# JPEG_IMAGES = []
# PNG_IMAGES = []
# JPG_IMAGES = []
# SVG_IMAGES = []

# AVI_MEDIA = []
# MP4_MEDIA = []
# MOV_MEDIA = []
# MKV_MEDIA = []

# MP3_MUSIC = []
# OGG_MUSIC = []
# WAV_MUSIC = []
# AMR_MUSIC = []

# DOC_DOCUMENT = []
# DOCX_DOCUMENT = []
# TXT_DOCUMENT = []
# PDF_DOCUMENT = []
# XLSX_DOCUMENT = []
# PPTX_DOCUMENT = []

# ZIP_ARCHIVE = []
# GZ_ARCHIVE = []
# TAR_ARCHIVE = []

# DIFFERENT = []


# # REGISTER_EXTENSIONS = {'JPEG': JPEG_IMAGES, 'PNG': PNG_IMAGES, 'JPG': JPG_IMAGES, 'SVG':SVG_IMAGES, 'AVI':AVI_MEDIA, 'MP4':MP4_MEDIA, 'MOV': MOV_MEDIA, 'MKV':MKV_MEDIA, 'DOC':DOC_DOCUMENT, 'DOCX': DOCX_DOCUMENT, 'TXT': TXT_DOCUMENT, 'PDF': PDF_DOCUMENT, 'XLSX': XLSX_DOCUMENT, 'PPTX': PPTX_DOCUMENT, 'MP3': MP3_MUSIC, 'OGG': OGG_MUSIC, 'WAV': WAV_MUSIC, 'AMR': AMR_MUSIC, 'ZIP': ZIP_ARCHIVE, 'GZ': GZ_ARCHIVE, 'TAR': TAR_ARCHIVE}

# FOLDERS = []
# EXTENSIONS = set()
# UNKNOWN = set()

# def get_extension(filename: str) -> str:
#     # print(filename)
#     return Path(filename).suffix[1:].upper()


# def scan(folder: Path) -> None:
#     for item in folder.iterdir():
#         if item.is_dir():
#             if item.name not in ('archives', 'video', 'audio', 'documents', 'images', 'different'):
#                 FOLDERS.append(item)
#                 scan(item)
#             continue

        
#         ext = get_extension(item.name)
#         # print(ext)
#         fullname = folder / item.name
#         if not ext:
#             DIFFERENT.append(fullname)
#         else:    
#             try:
#                 container = REGISTER_EXTENSIONS[ext]
#                 print(container)
#                 EXTENSIONS.add(ext)
#                 container.append(fullname)
#             except KeyError:
#                 UNKNOWN.add(ext)
#                 DIFFERENT.append(fullname)
 
# if __name__ == '__main__':
#     folder_for_scan = sys.argv[1]
#     print(f'Start in folder {folder_for_scan}')

#     scan(Path(folder_for_scan))

#     print(f'Images jpeg: {JPEG_IMAGES}')
#     print(f'Images jpg: {JPG_IMAGES}')
#     print(f'Images svg: {SVG_IMAGES}')
#     print(f'Audio mp3: {MP3_MUSIC}')
#     print(f'Archives: {ZIP_ARCHIVE}')

#     print(FOLDERS[::-1])