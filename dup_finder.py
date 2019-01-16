"""
Find paths to files with identical contents . Currently supports either MD5 or files sizes to check.

TODO: Add flag for verifying name of files as well

Usage:
    python dup_finder.py <PATH or FS URL> [-s | -m]

Example:

    python dup_finder.py ~/github -s

    python dup_finder.py /Users/Phon3/Downloads -m


"""

#!/usr/bin/python
__author__ = 'Phon3'
import argparse
from collections import defaultdict
import hashlib
import sys, os.path
from fs import open_fs

def get_hash(bin_file):
    """Get the md5 hash of a file."""
    file_hash = hashlib.md5()
    while True:
        chunk = bin_file.read(1024 * 1024)
        if not chunk:
            break
        file_hash.update(chunk)
    return file_hash.hexdigest()

def get_size(bin_file):
    return os.path.getsize(bin_file)

def check_dup(location, input_type):
    hashes = defaultdict(list)
    fsize = defaultdict(list)
    with open_fs(location) as fs:
        for path in fs.walk.files():
            file_size = get_size(location + path)
            with fs.open(path, "rb") as bin_file:
                
                file_hash = get_hash(bin_file)
            hashes[file_hash].append(path)
            fsize[file_size].append(path)

    if input_type == 1:
        for paths in hashes.values():
            if len(paths) > 1:
                for path in paths:
                    print(f" {path}")
                print()
    else:  ##Need to add a query for file size & names too, not just file size.
        for input_files in fsize.values():
            if len(input_files) > 1:
                for files in input_files:
                    print(f" {files}")
                print()                


def main():
    # Instantiate the parser
    parser = argparse.ArgumentParser(description='Ex: python3 dup_finder.py ~/mysite')
    parser.add_argument('location', 
                        help='the directory you want to search for Duplicates')
    group_parser = parser.add_mutually_exclusive_group()
    group_parser.add_argument("-s", "--size", dest="input_size", action = "store_true",
                    help="Check for dupes using File Size")
    group_parser.add_argument("-m", "--md5", dest="input_md5", action = "store_false",
                    help="Check for dupes using MD5 Hashes (Default)")
    args = parser.parse_args()
    #Check for input type, MD5 or File Size
    if args.input_size == True:
        input_type = 0
    else:
        input_type = 1

    #Quick dirty check to see if the directory exists
    if not os.path.exists(args.location):
        print("You are trying to look in a Directory that doesn't exist.")
    else:
        check_dup(args.location, input_type)

if __name__ == "__main__":
    main()
