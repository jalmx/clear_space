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

    new_full_path= ""
    new_name = name.strip().replace(old_sep, new_sep)

    if full_path.count(name) > 1:  # if father folder have the same name as child
        path_base = full_path.split(os.path.sep)[0:-1]
        base_path = os.path.sep.join(path_base) + os.path.sep
        new_full_path = f"{base_path}{new_name}"
    else:
        new_full_path = full_path.replace(name, new_name)

    os.rename(full_path, new_full_path)
    print(full_path, "++>", new_full_path)
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


def clear_space(path: Path, old_sep=" ", new_sep="_", is_change_file=True, is_change_folder=False, is_recursive=False):
    # Principal function from the module
    files, directories = (None, None)
    item = Path(path)

    if item.is_dir():
        files, directories = read_files_from_folder(path=path, is_recursive=is_recursive)["all"]
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
    Just for the module
    :return:
    """
    # path = Path("./assets")
    # path = Path(f"./assets/folder uno{os.path.sep}main uno.py")
    path = Path(f"/home/xizuth/Projects/clear_space/test")
    clear_space(path, is_change_file=True, is_change_folder=True, is_recursive=True)


if __name__ == "__main__":
    main()
