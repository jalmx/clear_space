#!/usr/bin/env python3

"""
JUST FOR DEVELOP THE cli, NO FOR RELEASE
"""
import argparse
import pathlib

from clear_space import clear_space

example = """Examples to use:

cspace "file name"
cspacex -r ./ -> apply all files and search in folders
scapcex ./ [default apply all files in this folder]
cspacex -d -r ./ [change all files and folders recursive]
cspacex -d -r --no-file ./ change just name folders recursive

cspacex "file-one" --old-sep - --new_sep _ [gonna change all (-) for (_)]
    result: file_one
"""

verbose = False


def cli():
    try:
        parser = argparse.ArgumentParser(description='Tool for change a symbol from name files or folders',
                                         formatter_class=argparse.RawDescriptionHelpFormatter, epilog=example)

        parser.add_argument("path", metavar="file or path", type=pathlib.Path, help="File or path to change name")
        parser.add_argument("--no-file", default=False, action="store_true", help="No include files")
        parser.add_argument("-d", "--directory", default=False, action="store_true",
                            help="Indicate if include directories " "change name")
        parser.add_argument("-v", "--verbose", default=False, action="store_true", help="Show all logs")
        parser.add_argument("-r", "--recursive", default=False, action="store_true",
                            help="Search recursive inside folders")
        parser.add_argument("--old-sep", type=str, default=" ", help="Old separator. Default space")
        parser.add_argument("--new-sep", type=str, default="_", help="New separator. Default underscore")

        parser.add_argument('--version', action='version', version='0.0.1')

        args = parser.parse_args()
        global verbose
        verbose = args.verbose

        print(args)

        # exit(1)
        clear_space(path=args.path, is_change_file=(not args.no_file), is_change_folder=args.directory,
                    is_recursive=args.recursive,
                    old_sep=args.old_sep, new_sep=args.new_sep, debug=args.verbose)
        print("*Done*")

    except Exception as e:
        print("Something was wrong, if you want view the log, use `--verborse`")
        if verbose:
            print(e)


def main():
    # To test cli.py
    cli()


if __name__ == "__main__":
    main()
