import os.path
import sys
from pathlib import Path
from file_parser import arrange_files_sorting_in_folder

def main():
    try:
        target_folder = sys.argv[1]
    except IndexError:
        print('Folder for sorting was not defined. Please enter path to folder.')
        return
    
    if not os.path.exists(target_folder):
        print('Indicated folder doesn\'t exist. Please check path and start process again')
        exit()
    
    print(f'\nWe start file sorting process in folder -> {target_folder}\n')
    arrange_files_sorting_in_folder(target_folder)
    print(f'Sorting process in progress...\n')
    print(f"Files were sorted successfully. Please check here -> {target_folder}\n")

if __name__ == "__main__":
    main()


"""old version"""
# # Homework
# from pathlib import Path
# import shutil
# import sys
# import file_parser as parser
# from normalize import normalize

# def handle_files(filename: Path, target_folder: Path):
#     target_folder.mkdir(exist_ok=True, parents=True)
#     filename.replace(target_folder / normalize(filename.name))

# def handle_archive(filename: Path, target_folder: Path):
#     target_folder.mkdir(exist_ok=True, parents=True)
#     folder_for_file = target_folder / normalize(filename.name.replace(filename.suffix, ''))
#     folder_for_file.mkdir(exist_ok=True, parents=True)
    
#     try:
#         shutil.unpack_archive(str(filename.resolve()), str(folder_for_file.resolve()))
#     except shutil.ReadError:
#         folder_for_file.rmdir()
#         return None
#     filename.unlink()


# def handler_folder(folder: Path):
#     try:
#         folder.rmdir()
#     except OSError:
#         print(f"Is folder didn't delete {folder}")

# def main(folder: Path):
#     parser.scan(folder)

#     for file in parser.JPEG_IMAGES:
#         handle_files(file, folder / 'images')
#     for file in parser.PNG_IMAGES:
#         handle_files(file, folder / 'images')
#     for file in parser.JPG_IMAGES:
#         handle_files(file, folder / 'images')
#     for file in parser.SVG_IMAGES:
#         handle_files(file, folder / 'images')
    
#     for file in parser.AVI_MEDIA:
#         handle_files(file, folder / 'media')
#     for file in parser.MP4_MEDIA:
#         handle_files(file, folder / 'media')
#     for file in parser.MOV_MEDIA:
#         handle_files(file, folder / 'media')
    
#     for file in parser.MP3_MUSIC:
#         handle_files(file, folder / 'music')
#     for file in parser.OGG_MUSIC:
#         handle_files(file, folder / 'music')
#     for file in parser.WAV_MUSIC:
#         handle_files(file, folder / 'music')
#     for file in parser.AMR_MUSIC:
#         handle_files(file, folder / 'music')
    
#     for file in parser.DOC_DOCUMENT:
#         handle_files(file, folder / 'documents')
#     for file in parser.DOCX_DOCUMENT:
#         handle_files(file, folder / 'documents')   
#     for file in parser.TXT_DOCUMENT:
#         handle_files(file, folder / 'documents')
#     for file in parser.PDF_DOCUMENT:
#         handle_files(file, folder / 'documents')
#     for file in parser.XLSX_DOCUMENT:
#         handle_files(file, folder / 'documents')
#     for file in parser.PPTX_DOCUMENT:
#         handle_files(file, folder / 'documents')
    
#     for file in parser.ZIP_ARCHIVE:
#         handle_archive(file, folder / 'archives')
#     for file in parser.GZ_ARCHIVE:
#         handle_archive(file, folder / 'archives')
#     for file in parser.TAR_ARCHIVE:
#         handle_archive(file, folder / 'archives')

#     for file in parser.DIFFERENT:
#         handle_files(file, folder / 'different')

#     for folder in parser.FOLDERS[::-1]:
#         handler_folder(folder)


# if __name__ == '__main__':
#     if sys.argv[1]:
#         folder_for_scan = Path(sys.argv[1])
#         print(f'Start in folder {folder_for_scan.resolve()}')
#         main(folder_for_scan.resolve())
