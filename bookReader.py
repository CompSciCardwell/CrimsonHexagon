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
        #print(cleantext + "-")
        outputtext += cleantext
    print(outputtext)
    return outputtext


def addToDict( dictionary, inputText ):
    for line in inputText.split():
        #print(line + "-")
        for word in line.split(" "):
            if not word in dictionary:
                dictionary[word] = 1
            else:
                dictionary[word] += 1

    for keys, values in dictionary.items():
        print(keys)
        print(values)

    return dictionary

set = {}

rootdir = Path('/home/compscicardwell/SpiderOak Hive/Actual Documents/Git/CrimsonHexagon/Data Sets/Fantasy/Eric - Terry Pratchett.epub')

#singleBook(rootdir)

addToDict(set, singleBook(rootdir))
print(set)

#file_list = [f for f in rootdir.glob('**/*') if f.is_file() and f.suffix == '.epub']

#for f in file_list:
    #print(f)
    #book = epub.read_epub(f)
    #for item in book.get_items_of_type(ebooklib.ITEM_DOCUMENT):
        #print('NAME : ', item.get_name())
        #cleantext = BeautifulSoup(item.get_content(), "lxml").text
        #cleantext = re.sub(r'[^\w\s]', '', cleantext)
        #print(cleantext.lower())