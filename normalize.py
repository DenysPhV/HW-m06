import re
import sys

CYRILLIC_SYMBOLS = "абвгдеёжзийклмнопрстуфхцчшщъыьэюяєіїґ"
TRANSLATION = ("a", "b", "v", "g", "d", "e", "e", "j", "z", "i", "j", "k", "l", "m", "n", "o", "p", "r", "s", "t", "u",
               "f", "h", "ts", "ch", "sh", "sch", "", "y", "", "e", "yu", "ya", "je", "i", "ji", "g")


TRANS = {}
for cyr, lat in zip(CYRILLIC_SYMBOLS, TRANSLATION):
        TRANS[ord(cyr)] = lat
        TRANS[ord(cyr.upper())] = lat.upper()


def normalize(name: str) -> str:
        # we make transliteration of cyrillic letters to latin
        t_name = name.translate(TRANS)
        idx = t_name.rfind('.')
        # change unknown symbols on '_'
        t_name = re.sub(r'\W', '_', t_name[0:idx]) + t_name[idx:]
        return t_name


if __name__ == "__main__":
        file_for_normalize = sys.argv[1]
        print(normalize(file_for_normalize))
 