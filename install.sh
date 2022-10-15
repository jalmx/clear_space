#!/bin/bash

./build.sh
cp ./bin/* $HOME/.local/bin

echo "Add to PATH $HOME/.local/bin, if you have done, ignore this message"