#!/usr/bin/env python3

from pathlib import Path
import os

DEBUG = True

# FIX: to search recursive


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

    if DEBUG:
        print(f"Folders: {len(directories_path)} & Files: {len(files_path)} in \"{path}\"")

    return {
        "files": files_path,
        "directories": directories_path
    }


def change_name(path: Path, old_sep=" ", sep="_", is_change_name=True):
    if not is_change_name:
        return

    full_path = os.path.abspath(path)
    name = full_path.split(os.path.sep)[-1]
    new_name = name.strip().replace(old_sep, sep)
    new_full_path = full_path.replace(name, new_name)
    os.rename(full_path, new_full_path)

    if DEBUG:
        print(full_path, new_full_path)


def clear_space(path: Path, is_change_file=True, is_change_folder=False):
    change_name(path)


def main():
    #path = Path("./assets")
    #path = Path(f"./assets/folder uno{os.path.sep}main uno.py")
    path = Path(f"./assets/folder dos ")
    clear_space(path)


if __name__ == "__main__":
    main()
