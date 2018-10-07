import ebooklib
from ebooklib import epub
from pathlib import Path
from bs4 import BeautifulSoup
import re

def singleBook( location ):
    myDir = location
    book = epub.read_epub(myDir)
    items = book.get_items_of_type(ebooklib.ITEM_DOCUMENT)
    outputtext = ""
    for item in items:
        cleantext = BeautifulSoup(item.get_content(), "lxml").text
        cleantext = re.sub(r'[^\w\s]', '', cleantext)
        cleantext = cleantext.lower()
        outputtext += cleantext
    print(outputtext)
    return outputtext


def addToDict( dictionary, inputText ):
    for line in inputText.split():
        for word in line.split(" "):
            if not word in dictionary:
                dictionary[word] = 1
            else:
                dictionary[word] += 1

    for keys, values in dictionary.items():
        print(keys)
        print(values)

    return dictionary

def trainDirectory( pathname )
    rootdir = Path(pathname)
    set = {}

    file_list = [f for f in rootdir.glob('**/*') if f.is_file() and f.suffix == '.epub']

    for f in file_list:
        book = epub.read_epub(f)
        addToDict(set, singleBook(f))
