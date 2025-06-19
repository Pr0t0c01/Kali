#!/bin/bash

while getopts i:o: flag
do
    case "${flag}" in
        i) inputfile=${OPTARG};;
        o) outputfile=${OPTARG};;
    esac
done

# Define the input file

# Read the input file line by line
while read -r LINE
do
    assetfinder "$LINE" -subs-only >> "$outputfile"
done < "$inputfile"
