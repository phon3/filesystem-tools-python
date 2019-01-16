"""
Display how much storage is used on a hdd of a specific file type.

Usage:
    python count_bytes.py <FILE Type> <PATH or FS URL>

Example:
    HTML files: python count_bytes.py html ~/www

    JPG files: python count_bytes.py jpg ~/Downloads

    PDF files: python count_bytes.py pdf /Users/Phon3/Ebooks
"""

#!/usr/bin/python
__author__ = 'Phon3'
import argparse
from fs import open_fs
from fs.filesize import traditional


def main():
    count= 0
    # Instantiate the parser
    parser = argparse.ArgumentParser(description='Ex: python3 count_bytes.py html ~/mysite')
    parser.add_argument('action', type=str,
                        help='the FILE type you are looking for e.g. html, py, jpg')
    parser.add_argument('location', type=str,
                        help='directory where you want to search')
    args = parser.parse_args()

    #open_fs will now parse the file type through the specified directory & sub directories
    fs_type = "*." + args.action
    with open_fs(args.location) as fs:
        for _path, info in fs.walk.info(filter=[fs_type], namespaces=["details"]):
            count += info.size
    print(f'There is {traditional(count)} of "{args.action}" files in "{args.location}"')


if __name__ == "__main__":
    main()