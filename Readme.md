# Clear space

Script for change name for files in folder. All files change just the space in the name for another symbol.

**No dependencies**

## how to use

```commandline
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

