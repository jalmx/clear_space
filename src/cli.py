#!/usr/bin/env python3

import argparse

"""
help

-r mode recursive
-d apply to directories
-f apply to files
-v verbose

--old-sep - [default: space]
--new-sep _ [default: underscore]

Examples to use:

cspace file name
cspacex ./ -f -r -> apply all files and search in folders
scapcex ./ -f [default apply all files in the folder]
cspacex ./ -f -d -r [change all files and folders recursive]
cspacex ./ -d -r [change the name all from directories recursive]

cspacex "file-one" --old-sep - --new_sep _ [gonna change all (-) for (_)]
    result: file_one

"""

def main():
    pass
