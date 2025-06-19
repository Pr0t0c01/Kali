#!/bin/bash

read -p "Your File(.txt) : " file;
while read -r line; do
    echo -e "$line"
done < "$file";
