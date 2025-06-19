#!/bin/bash
read -p "Your Amass Subdomain File(.txt) : " file;
grep -oE '([A-Za-z0-9-]+\.){1,3}[A-Za-z0-9-]+\.[A-Za-z]{2,6}' $file | awk -F. '{print $(NF-2) "." $(NF-1) "." $NF}' | sort -u
