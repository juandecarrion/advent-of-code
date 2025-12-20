#!/bin/sh


# Inspired by https://github.com/jonathanpaulson/AdventOfCode/blob/master/get_input.py

source .env

if [ "$#" -ne 2 ];
    then echo "Wrong number of parameters, please use $0 <year> <day>"
    exit 1
fi


URL=https://adventofcode.com/"$1"/day/"$2"/input
DIR=./"$1"

mkdir -p "$DIR"
curl "$URL" \
  --cookie "session=$SESSION" \
  -o "$DIR"/"$2".txt
