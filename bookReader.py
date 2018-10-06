import ebooklib
from ebooklib import epub
from pathlib import Path
from bs4 import BeautifulSoup
import re

def singleBook( location ):
    rootdir = Path(location)
    book = epub.read_epub(rootdir)
    for item in book.get_items_of_type(ebooklib.ITEM_DOCUMENT):
        cleantext = BeautifulSoup(item.get_content(), "lxml").text
        cleantext = re.sub(r'[^\w\s]', '', cleantext)
        cleantext = cleantext.lower()
        print(cleantext)

def addToDict( dictionary, inputText ):
    

set = {}

rootdir = Path('/home/compscicardwell/SpiderOak Hive/Actual Documents/Git/CrimsonHexagon/Data Sets/Fantasy/Eric - Terry Pratchett.epub')

singleBook(rootdir)

#file_list = [f for f in rootdir.glob('**/*') if f.is_file() and f.suffix == '.epub']

#for f in file_list:
    #print(f)
    #book = epub.read_epub(f)
    #for item in book.get_items_of_type(ebooklib.ITEM_DOCUMENT):
        #print('NAME : ', item.get_name())
        #cleantext = BeautifulSoup(item.get_content(), "lxml").text
        #cleantext = re.sub(r'[^\w\s]', '', cleantext)
        #print(cleantext.lower())