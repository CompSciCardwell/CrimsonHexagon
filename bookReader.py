import ebooklib
from ebooklib import epub
from pathlib import Path
from bs4 import BeautifulSoup

def dumpDirectoryOfBooks( location ):
    rootdir = Path(location)

    file_list = [f for f in rootdir.glob('**/*') if f.is_file() and f.suffix == '.epub']

    for f in file_list:
        print(f)
        book = epub.read_epub(f)

def singleBook( location ):
    rootdir = Path(location)

    file_list = [f for f in rootdir.glob('**/*') if f.is_file() and f.suffix == '.epub']

    for f in file_list:
        print(f)
        book = epub.read_epub(f)

rootdir = Path('/home/compscicardwell/SpiderOak Hive/Actual Documents/Git/CrimsonHexagon/Data Sets/Fantasy')

file_list = [f for f in rootdir.glob('**/*') if f.is_file() and f.suffix == '.epub']

for f in file_list:
    print(f)
    book = epub.read_epub(f)
    for item in book.get_items_of_type(ebooklib.ITEM_DOCUMENT):
        print('NAME : ', item.get_name())
        cleantext = BeautifulSoup(item.get_content(), "lxml").text
        print(cleantext)