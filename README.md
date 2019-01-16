Filesystem Tools Python
======================

A simple to use command line interface for python. You can check for file sizes of a specific type or check for duplicates of files is certain directories. This utilitizes the PyFilesystem (fs) for ease of use and functionality.

Dependencies:

PyFilesystem - fs

Installation:
```
pip install fs
```



###dup_finder.py

Find paths to files with identical contents . Currently supports either MD5 or files sizes to check.

TODO: Add flag for verifying name of files as well

Usage:
```
    python dup_finder.py <PATH or FS URL> [-s | -m]
```

Example:

File Size :`python dup_finder.py ~/github -s`

MD5 Hashes: `python dup_finder.py /Users/Phon3/Downloads -m`



###count_bytes.py

Display how much storage is used on a hdd of a specific file type.

Usage:
```
    python count_bytes.py <FILE Type> <PATH or FS URL>
```

Example:

HTML files: `python count_bytes.py html ~/www`

JPG files: `python count_bytes.py jpg ~/Downloads`

PDF files: `python count_bytes.py pdf /Users/Phon3/Ebooks`