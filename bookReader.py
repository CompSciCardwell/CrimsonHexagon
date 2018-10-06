import ebooklib
from ebooklib import epub
from pathlib import Path

rootdir = Path('/home/compscicardwell/SpiderOak Hive/Actual Documents/Git/CrimsonHexagon/Data Sets/Fantasy')

file_list = [f for f in rootdir.glob('**/*') if f.is_file() and f.suffix == '.epub']

for f in file_list:
    print(f)
    book = epub.read_epub(f)