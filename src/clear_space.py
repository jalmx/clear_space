#!/usr/bin/env python3

import argparse
import os
from pathlib import Path

DEBUG = False


def read_files_from_folder(path: Path, is_recursive=False) -> dir:
    """
    This function read all files and folders
    :param path: Path from folder to search
    :param is_recursive: Going to search all files in from recursive
    :return: a dict with 2 list with a files and folders
    """
    files_path = []
    directories_path = []

    for item in path.iterdir():
        if item.is_file():
            files_path.append(item)
        if item.is_dir():
            directories_path.append(item)
            if is_recursive:
                _file, _directories = read_files_from_folder(item, is_recursive)["all"]
                if len(_file) > 0:
                    files_path.extend(_file)
                if len(_directories) > 0:
                    directories_path.extend(_directories)

    if DEBUG:
        print(f"Folders: {len(directories_path)} & Files: {len(files_path)} in \"{path}\"")

    return {
        "files": files_path,
        "directories": directories_path,
        "all": [files_path, directories_path]
    }


def swap_list(items: list):
    return [items[i] for i in range(len(items) - 1, -1, -1)]


def change_name(path: Path, old_sep=" ", new_sep="_") -> bool:
    """
    Change name from a file or folder
    :param path: Path from file or folder
    :param old_sep: old separator, default [one space]
    :param new_sep: new separator, default (_)
    :return: None
    """

    full_path = os.path.abspath(path)
    name = full_path.split(os.path.sep)[-1]

    if name.find(old_sep) == -1:
        return False

    new_full_path = ""
    new_name = name.strip().replace(old_sep, new_sep)

    if full_path.count(name) > 1:  # if father folder have the same name as child
        path_base = full_path.split(os.path.sep)[0:-1]
        base_path = os.path.sep.join(path_base) + os.path.sep
        new_full_path = f"{base_path}{new_name}"
    else:
        new_full_path = full_path.replace(name, new_name)

    os.rename(full_path, new_full_path)

    if DEBUG:
        print(full_path, "-->", new_full_path)

    return True


def change_name_all_files(files_path: [], old_sep=" ", new_sep="_"):
    count = 0
    for file_path in files_path:
        is_change = change_name(file_path, old_sep=old_sep, new_sep=new_sep)

        if is_change:
            count += 1

    if DEBUG:
        print(f"Changed {count}")


def clear_space(path: Path, old_sep=" ", new_sep="_", is_change_file=True, is_change_folder=False, is_recursive=False,
                debug=True) -> None:
    """
    Principal function from this module
    :param path: Path folder or file
    :param old_sep: Old separator
    :param new_sep: New separator to change
    :param is_change_file: if apply changes to file
    :param is_change_folder: if apply change to folder
    :param is_recursive: is going to search all files and folder inside another
    :param debug: mode verbose
    :return: None
    """

    global DEBUG
    DEBUG = debug
    files, directories = (None, None)
    item = Path(os.path.abspath(path))

    if item.is_dir():
        files, directories = read_files_from_folder(path=item, is_recursive=is_recursive)["all"]
        if DEBUG:
            print(f"files: {len(files)}, Folders: {len(directories)}")
        if is_change_file:
            change_name_all_files(files, old_sep=old_sep, new_sep=new_sep)
        if is_change_folder:
            # I have to swap all folders for avid to crash, because if it has changed name folder father,
            # crash to rename name for folder child
            change_name_all_files(swap_list(directories), old_sep=old_sep, new_sep=new_sep)
    else:
        change_name(item, old_sep=old_sep, new_sep=new_sep)


def main():
    """
    Just for test the module
    :return: None
    """
    # path = Path("./assets")
    # path = Path(f"./assets/folder uno{os.path.sep}main uno.py")
    path = Path(f"./")
    clear_space(path, old_sep="-", new_sep="_", is_change_file=True, is_change_folder=False, is_recursive=False,
                debug=True)


### ------------------ cli --------------------------------

example = """Examples to use:

cspace "file name"
cspacex -r ./ -> apply all files and search in folders
scapcex ./ [default apply all files in this folder]
cspacex -d -r ./ -> change all files and folders recursive
cspacex -d -r --no-file ./ ->change just name folders recursive
cspacex --no-file -d ./ -> change name just folders, no files
 
cspacex "file-one" --old-sep - --new_sep * [gonna change all (-) for (_)]
    result: file_one
"""


def cli():
    try:
        parser = argparse.ArgumentParser(description='Tool for change a symbol from name files or folders',
                                         formatter_class=argparse.RawDescriptionHelpFormatter, epilog=example)

        parser.add_argument("path", metavar="file or path", type=Path, help="File or path to change name")
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

        # print(args)

        clear_space(path=args.path, is_change_file=(not args.no_file), is_change_folder=args.directory,
                    is_recursive=args.recursive,
                    old_sep=args.old_sep, new_sep=args.new_sep, debug=args.verbose)
        print("*Done*")

    except Exception as e:
        print("Something was wrong, if you want view the log, use `--verborse`")
        if verbose:
            print(e)


if __name__ == "__main__":
    cli()
