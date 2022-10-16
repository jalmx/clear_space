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
        "directories": directories_path,
        "all": [files_path, directories_path]
    }


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

    new_name = name.strip().replace(old_sep, new_sep)
    new_full_path = full_path.replace(name, new_name)
    os.rename(full_path, new_full_path)

    print(full_path, "-->", new_full_path)
    if DEBUG:
        # Message for Logs
        pass
    return True


def change_name_all_files(files_path: [], old_sep=" ", new_sep="_"):
    count = 0
    for file_path in files_path:
        is_change = change_name(file_path, old_sep=old_sep, new_sep=new_sep)

        if is_change:
            count += 1

    print(f"Changed {count}")

    if DEBUG:
        # Add message for log
        pass


def clear_space(path: Path, old_sep=" ", new_sep="_", is_change_file=True, is_change_folder=False):
    # Principal function from the module
    files, directories = (None, None)
    item = Path(path)

    if item.is_dir():
        files, directories = read_files_from_folder(path=path)["all"]
        if is_change_file:
            change_name_all_files(files)
        if is_change_folder:
            change_name_all_files(directories)
    else:
        change_name(item, old_sep=old_sep, new_sep=new_sep)


def main():
    """
    Just for the module
    :return:
    """
    # path = Path("./assets")
    # path = Path(f"./assets/folder uno{os.path.sep}main uno.py")
    path = Path(f"/home/xizuth/Projects/clear_space/test")
    clear_space(path, is_change_file=True, is_change_folder=True)


if __name__ == "__main__":
    main()
