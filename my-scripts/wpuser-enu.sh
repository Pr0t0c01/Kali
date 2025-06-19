read -p "Target URL: " url;
read -p "Number of Username: " num_user;
for i in $(seq 1 $num_user);
    do curl -s -L -i "$url?author=$i" | grep -E -o "\" title=\"View all posts by [a-z0-9A-Z\-\.]*|Location:.*" | sed 's/\// /g' | cut -f 6 -d ' ' | grep -v "^$";
done
