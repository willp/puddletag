import logging
import re

from PyQt5.QtWidgets import QApplication


class UnicodeMod(str):
    """Emulates the arg method of QStrings. Not meant for use anywhere other
    than the translate function above."""

    def arg(self, value):
        matches = [z for z in re.finditer(r"%(\d+)", self)]
        if not matches:
            logging.error('Undefined result for arg.')
            return UnicodeMod(self[::])
        elif len(matches) == 1:
            lowest = matches[0]
        else:
            lowest = sorted(matches, key=lambda m: m.groups())[0]
        text = lowest.group()
        if isinstance(text, bytes):
            text = text.decode('utf8', 'replace')
        if isinstance(value, bytes):
            value = value.decode('utf8', 'replace')
        elif isinstance(value, int):
            value = str(value)
        return UnicodeMod(self.replace(lowest.group(), value))

    def __add__(self, other):
        return UnicodeMod(str.__add__(self, other))

    def __radd__(self, other):
        return UnicodeMod(other.__add__(str(self)))

    def __mod__(self, other):
        return UnicodeMod(str.__mod__(self, other))

    def __format__(self, fmt=None):
        return UnicodeMod(str.__format__(self, fmt))

    def __getitem__(self, item):
        return UnicodeMod(str.__getitem__(self, item))

    def __rmul__(self, v):
        return UnicodeMod(str.__rmul__(self, v))

    def __mul__(self, v):
        return UnicodeMod(str.__mul__(self, v))


def translate(k, v):
    if isinstance(v, bytes):
        v = v.decode('utf8', 'replace')
    try:
        return UnicodeMod(QApplication.translate(k, v))
    except TypeError:
        return v


def dont_execute():
    # General Translations
    translate("GenSettings", 'Su&bfolders')
    translate("GenSettings", 'Show &gridlines')
    translate("GenSettings", 'Show tooltips in file-view:')
    translate("GenSettings", 'Show &row numbers')
    translate("GenSettings", 'Automatically resize columns to contents')
    translate("GenSettings", '&Preserve file modification times')
    translate("GenSettings", 'Program to &play files with:')
    translate("GenSettings", '&Load last folder at startup')

    # Artwork
    translate("Artwork Context", 'Cover Varies')
    translate("Artwork Context", 'No Images')

    # Menus
    translate("Menus", 'Enabl&e Preview Mode')
    translate("Menus", 'Clear Selected &Files')
    translate("Menus", '&Write Previews')
    translate("Menus", '&Undo Last Clear')
    translate("Menus", 'Sort &By')
    translate("Menus", 'Clear Selected &Cells')
    translate("Menus", "&Plugins")
    translate("Menus", "Sort &By")
    

    #Functions
    translate("Functions", "Artwork: Filenames='$1', Description='$2', Case Sensitive=$3")
    translate("Functions", "Load Artwork")
    translate("Functions", "&Filenames to check (;-separated, shell wildcards [eg. *] allowed)")
    translate("Functions", "&Default description (can be pattern):")
    translate("Functions", "Match filename's &case:")
    translate("Functions", "Autonumbering: $0, Start: $1, Restart for dir: $2, Padding: $3")
    translate("Functions", "Autonumbering")
    translate("Functions", "oi")
    translate("Functions", "1")
    translate("Functions", "aoeu")
    translate("Functions", "False")
    translate("Functions", "au")
    translate("Functions", "1")
    translate("Functions", "Convert to encoding: $0, Encoding: $1")
    translate("Functions", "Convert from non-standard encoding")
    translate("Functions", "&Encoding")
    translate("Functions", "cp1250")
    translate("Functions", "cp1251")
    translate("Functions", "cp1252")
    translate("Functions", "cp1253")
    translate("Functions", "cp1254")
    translate("Functions", "cp1255")
    translate("Functions", "cp1256")
    translate("Functions", "cp1257")
    translate("Functions", "cp1258")
    translate("Functions", "euc_jp")
    translate("Functions", "cp932")
    translate("Functions", "euc_jis_2004")
    translate("Functions", "shift_jis")
    translate("Functions", "johab")
    translate("Functions", "big5")
    translate("Functions", "big5hkscs")
    translate("Functions", "gb2312")
    translate("Functions", "gb18030")
    translate("Functions", "gbk")
    translate("Functions", "hz")
    translate("Functions", "File->Tag '$1'")
    translate("Functions", "Filename to Tag")
    translate("Functions", "&Pattern")
    translate("Functions", "Format $0 using $1")
    translate("Functions", "Format value")
    translate("Functions", "&Format string")
    translate("Functions", "Text File: $0, '$1'")
    translate("Functions", "Import text file")
    translate("Functions", "&Pattern (can be relative path)")
    translate("Functions", "lyrics.txt")
    translate("Functions", "Merge field: $0, sep='$1'")
    translate("Functions", "Merge field")
    translate("Functions", "&Separator")
    translate("Functions", ";")
    translate("Functions", "Tag->File: $1")
    translate("Functions", "Tag to filename")
    translate("Functions", "&Pattern")
    translate("Functions", "Remove Dupes: $0, Match Case $1")
    translate("Functions", "Remove duplicate values")
    translate("Functions", "Match &Case")
    translate("Functions", "Remove fields except: $1")
    translate("Functions", "Remove all fields except")
    translate("Functions", "&Field list (; separated):")
    translate("Functions", "")
    translate("Functions", "Replace $0: '$1' -> '$2', Match Case: $3, Words Only: $4")
    translate("Functions", "Replace")
    translate("Functions", "&Replace")
    translate("Functions", "w&ith:")
    translate("Functions", "Match c&ase:")
    translate("Functions", "only as &whole word")
    translate("Functions", "RegReplace $0: RegExp '$1' with '$2', Match Case: $3")
    translate("Functions", "Replace with RegExp")
    translate("Functions", "&Regular Expression")
    translate("Functions", "Replace &matches with:")
    translate("Functions", "Match &Case")
    translate("Functions", "Export Art: pattern='$1'")
    translate("Functions", "Export artwork to file")
    translate("Functions", "&Pattern (extension not required)")
    translate("Functions", "folder_%img_counter%")
    translate("Functions", "Sort $0, order='$1', Match Case='$2'")
    translate("Functions", "Sort values")
    translate("Functions", "&Order")
    translate("Functions", "Ascending")
    translate("Functions", "Descending")
    translate("Functions", "Match &Case")
    translate("Functions", "Split using separator $0: sep='$1'")
    translate("Functions", "Split fields using separator")
    translate("Functions", "&Separator")
    translate("Functions", ";")
    translate("Functions", "Trim $0")
    translate("Functions", "Trim whitespace")
    translate("Functions", "Tag->Dir: $1")
    translate("Functions", "Tag to Dir")
    translate("Functions", "&Pattern (can be relative path)")
    translate("Functions", "%artist% - %album%")
    translate("Functions", "Text to Tag: $0 -> $1, $2")
    translate("Functions", "Text to Tag")
    translate("Functions", "&Text")
    translate("Functions", "&Pattern")
    translate("Functions", "&Output")
    translate("Functions", "Convert Case: $0: $1")
    translate("Functions", "Case conversion")
    translate("Functions", "&Type")
    translate("Functions", "Mixed Case")
    translate("Functions", "UPPER CASE")
    translate("Functions", "lower case")
    translate("Functions", "For &Mixed Case, after any of:")
    translate("Functions", "., !")
    translate("Functions", "<blank> $0")
    translate("Functions", "Remove Fields")
    translate("Functions", "Update from $2, Fields: $1")
    translate("Functions", "Update from tag")
    translate("Functions", "&Field list (; separated):")
    translate("Functions", "&Tag")
    translate("Functions", "APEv2")
    translate("Functions", "ID3")

    #Dialogs
    translate("Dialogs", "Tag Panel")
    translate("Dialogs", "Artwork")
    translate("Dialogs", "Filesystem")
    translate("Dialogs", "Filter")
    translate("Dialogs", "Tag Sources")
    translate("Dialogs", "Stored Tags")
    translate("Dialogs", "Logs")
    translate("Dialogs", "Mass Tagging")
    translate("Dialogs", "Functions")
    translate("Dialogs", "Actions")
