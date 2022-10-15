#!/bin/sh

#pip install python-minifier # if failed install this
NAME_SCRIPT="cspacex"

rm -rf bin

mkdir -p bin

pyminify ./src/clear_space.py --output ./bin/$NAME_SCRIPT
sudo chmod +x bin/$NAME_SCRIPT