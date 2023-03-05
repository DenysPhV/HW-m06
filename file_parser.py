import sys
from pathlib import Path

JPEG_IMAGES = []
PNG_IMAGES = []
JPG_IMAGES = []
SVG_IMAGES = []

AVI_MEDIA = []
MP4_MEDIA = []
MOV_MEDIA = []
MKV_MEDIA = []

MP3_MUSIC = []
OGG_MUSIC = []
WAV_MUSIC = []
AMR_MUSIC = []

DOC_DOCUMENT = []
DOCX_DOCUMENT = []
TXT_DOCUMENT = []
PDF_DOCUMENT = []
XLSX_DOCUMENT = []
PPTX_DOCUMENT = []

ZIP_ARCHIVES = []
GZ_ARCHIVES = []
TAR_ARCHIVES = []

DIFFERENT = []


REGISTER_EXTENSIONS = {'JPEG': JPEG_IMAGES, 'PNG': PNG_IMAGES, 'JPG': JPG_IMAGES, 'SVG':SVG_IMAGES, 'AVI':AVI_MEDIA, 'MP4':MP4_MEDIA, 'MOV': MOV_MEDIA, 'MKV':MKV_MEDIA, 'DOC':DOC_DOCUMENT, 'DOCX': DOCX_DOCUMENT, 'TXT': TXT_DOCUMENT, 'PDF': PDF_DOCUMENT, 'XLSX': XLSX_DOCUMENT, 'PPTX': PPTX_DOCUMENT, 'MP3': MP3_MUSIC, 'OGG': OGG_MUSIC, 'WAV': WAV_MUSIC, 'AMR': AMR_MUSIC, 'ZIP': ZIP_ARCHIVES, 'GZ': GZ_ARCHIVES, 'TAR': TAR_ARCHIVES}

FOLDERS = []
EXTENSIONS = set()
UNKNOWN = set()

def get_extension(filename: str) -> str:
    return Path(filename).suffix[1:].upper()

def scan(folder: Path) -> None:
    for item in folder.iterdir():
        if item.is_dir():
            if item.name not in ('archives', 'video', 'audio', 'documents', 'images', 'different'):
                FOLDERS.append(item)
                scan(item)
            continue

        ext = get_extension(item.name)
        fullname = folder / item.name
        if not ext:
            DIFFERENT.append(fullname)
        else:
            try:
                container = REGISTER_EXTENSIONS[ext]
                EXTENSIONS.add(ext)
                container.append(fullname)
            except KeyError:
                UNKNOWN.add(ext)
                DIFFERENT.append(fullname)
 
if __name__ == '__main__':
    folder_for_scan = sys.argv[1]
    print(f'Start in folder {folder_for_scan}')

    scan(Path(folder_for_scan))

    print(FOLDERS[::-1])