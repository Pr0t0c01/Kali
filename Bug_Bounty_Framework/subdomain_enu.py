#!/usr/bin/python3

import os
import sys
import subprocess

# Usage
# Run "python3 ./subdomain_enu.py <Dir-Path>"
# In <Dir-Path>, there must be "domain-scope.txt" which included domain-list for scope.
# 
# Eg - script is located in "tool". In "target" dir, there must be "domain-scope.txt"
# ┌──(shiroe㉿Shiroe)-[/home/user/tool/target]
# └─$ ls
# domain-scope.txt  subdomain.txt
#
# ┌──(shiroe㉿Shiroe)-[/home/user/tool]
# └─$ python3 ./subdomain_enu.py target

def Subdomain_Enu():
    target = sys.argv[1]
    target_file_path = os.path.join(target, "domain-scope.txt")
    if os.path.exists(target_file_path):
        
        print("="*10,f"Enumeration Subdomain","="*10)
        print("[+] AssetFinder ... ")
        subprocess.run(['bash', 'Tools/asset.sh', '-i', f'{target_file_path}', '-o', 'asset.txt'], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        
        print("[+] Subfinder ... ")
        subprocess.run(['subfinder', '-dL', f'{target_file_path}', '-o', 'subfind.txt', '-silent'], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

        print("[+] Alterx ... ")
        subprocess.run(['alterx', '-l', f'{target_file_path}', '-o', 'alterx.txt'], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

        print("[+] Merge Subdomains ... ")
        os.system(f'cat asset.txt subfind.txt alterx.txt | sort | uniq > {target}/merge_subdomain.txt')
        
        print("[+] Remove out of scope Subdomains ...") 
        os.system(f'python3 Tools/subdomain-scope.py {target}/merge_subdomain.txt {target}/subdomain.txt {target_file_path}')
        os.system(f'rm asset.txt alterx.txt subfind.txt {target}/merge_subdomain.txt')
        print("[+] subdomain.txt")
    else:
        print("File Not Found!")

Subdomain_Enu()
