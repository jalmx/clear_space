# Clear space

Script for change name for files in folder. All files change just the space in the name for another symbol.

**No dependencies**

## how to use

```commandline
help

usage: cspacex [-h] [--no-file] [-d] [-v] [-r] [--old-sep OLD_SEP] [--new-sep NEW_SEP] [--version] file or path

Tool for change a symbol from name files or folders

positional arguments:
  file or path       File or path to change name

optional arguments:
  -h, --help         show this help message and exit
  --no-file          No include files
  -d, --directory    Indicate if include directories change name
  -v, --verbose      Show all logs
  -r, --recursive    Search recursive inside folders
  --old-sep OLD_SEP  Old separator. Default space
  --new-sep NEW_SEP  New separator. Default underscore
  --version          show program's version number and exit

Examples to use:

cspace "file name"
cspacex -r ./ -> apply all files and search in folders
scapcex ./ [default apply all files in this folder]
cspacex -d -r ./ -> change all files and folders recursive
cspacex -d -r --no-file ./ ->change just name folders recursive
cspacex --no-file -d ./ -> change name just folders, no files
 
cspacex "file-one" --old-sep - --new_sep * [gonna change all (-) for (_)]
    result: file_one
```

## How to install

### Local

Exec script

```bash
./install
```

### Remote

**Install to PATH**

Just download and move to you want

```bash
wget -c https://raw.githubusercontent.com/jalmx/clear_space/master/bin/cspacex
```

**Install to PATH**

This way download to `$PATH` local

```bash
wget -c https://raw.githubusercontent.com/jalmx/clear_space/master/bin/cspacex -O $HOME/.local/bin/cspacex
```

> Note: Change permission to exe

```commandline
sudo chmod +x cspacex
```

## How to build

For build. you need to install `pyminifier` with `pip`:

```bash
pip install pyminifier
```

Then

Exec script

```bash
./build
```

You need to copy file `bin/cspacex` to `$PATH`

## Configuration workspace 

Create a venv, activate and install requirements.

```commandline
python3 -m venv 
source bin/activate
pip install -r requirements.txt
```

