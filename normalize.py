import re

CYRILLIC_SYMBOLS = "абвгдеёжзийклмнопрстуфхцчшщъыьэюяєіїґ"
TRANSLATION = ("a", "b", "v", "g", "d", "e", "e", "j", "z", "i", "j", "k", "l", "m", "n", "o", "p", "r", "s", "t", "u",
               "f", "h", "ts", "ch", "sh", "sch", "", "y", "", "e", "yu", "ya", "je", "i", "ji", "g")


TRANS = {}
for cs, l in zip(CYRILLIC_SYMBOLS, TRANSLATION):
        TRANS[ord(cs)] = l
        TRANS[ord(cs.upper())] = l.upper()


def normalize(name: str) -> str:
        t_name = name.translate(TRANS)
        t_name = re.sub(r'\W', '_', t_name)
        return t_name

 