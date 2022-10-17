#!/usr/bin/env python3

import argparse
from clear_space import clear_space
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

example = """Examples to use:

cspace file name
cspacex -f -r ./ -> apply all files and search in folders
scapcex -f ./ [default apply all files in the folder]
cspacex -f -d -r ./ [change all files and folders recursive]
cspacex -d -r ./ [change the name all from directories recursive]

cspacex "file-one" --old-sep - --new_sep _ [gonna change all (-) for (_)]
    result: file_one
"""
def cli():
    parser = argparse.ArgumentParser(description='Tool for change a symbol from name files or folders',
                                     formatter_class=argparse.RawDescriptionHelpFormatter, epilog="example")

    parser.add_argument("path", metavar="file or path", default="./",action="store_const",const="./" , help="File or path to change name")

    parser.add_argument("-f", "--file", default=True, action="store_true", help="File to change symbol")
    parser.add_argument("-d", "--directory", default=False, action="store_true", help="Indicate if include directories " "change name")
    parser.add_argument("-v", "--verbose", default=True, action="store_false", help="Show all logs")
    parser.add_argument("-r", "--recursive", default=False, action="store_false", help="Search recursive inside folders")
    parser.add_argument("--old-sep", type=str, default=" ",  help="Old separator. Default space")
    parser.add_argument("--new-sep", type=str, default="_", help="New separator. Default underscore")

    parser.add_argument('--version', action='version', version='0.0.1')

    args = parser.parse_args()

    print("argumentos:", args)

    clear_space(path=args.path, is_change_file=args.file, is_change_folder=args.directory, is_recursive=args.recursive, old_sep=args.old_sep, new_sep=args.new_sep,debug=args.verbose)
    #parser.print_help()


def main():
    # To test cli.py
    cli()

if __name__ == "__main__":
    main()