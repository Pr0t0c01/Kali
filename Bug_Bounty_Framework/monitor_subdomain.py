#!/usr/bin/python3

import os
import subprocess
import schedule
import time
import sys

### Usage 
#
## Base Folder
# ┌──(shiroe㉿Shiroe)-[/home/user/Kali/Python/Bug_Bounty_Framework]
# └─$ ls
#
# dreamsolution.nl  monitoring-list.txt  monitor_subdomain.py  Tools
# Tools - Include essential tools. 
# dreamsolution.nl - Recommend to use domain name. It's a dir to store result of monitoring result. If you want to monitor multi subdomain, create another dir like that.
# monitoring-list.txt - Filename is mandatory. Store list of dir name you want to monitor. In this case, it store dreamsolution.nl.
# 
## Monitor Folder
# ┌──(shiroe㉿Shiroe)-[/home/user/Bug_Bounty_Framework/dreamsolution.nl]
# └─$ ls
# domain-scope.txt  found_new_subdomain.txt  new.txt  old_subdomain.txt  old.txt  subdomain.txt
#
# domain-scope.txt - Filename is mandatory. Required for domain scope. No need wildcast. Eg - sony.com  
# old_subdomain.txt - Filename is mandatory. Required already scan result of subdomains. Need to import manually.
# found_new_subdomain.txt - It store new founded subdomains after scanning.

global target_list
target_list = []

def Check_Targets():
    with open('monitoring-list.txt','r') as file:
        for line in file:
            line = line.strip()
            target_list.append(line)

def Check_Old_File(target_list):
    for target in target_list:
        old_subdomain = os.path.join(target, "old_subdomain.txt")
        if os.path.exists(old_subdomain):
            print("[+] Found old subdomain file")
        else:
            print("[*] old_subdomain.txt Not Found!")
            sys.exit(1)

def Run_Each_Target(target_list):
    for target in target_list:
        Subdomain_Enu(target)

def Subdomain_Enu(target):
    target_file_path = os.path.join(target, "domain-scope.txt")
    if os.path.exists(target_file_path):
        
        print("="*10,f"Enumeration Subdomain for {target}","="*10)
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
        print("[*] domain-scope.txt Not Found!")

def Check_Newsubdomain(target_list):
    for target in target_list:
        os.system(f'cat {target}/subdomain.txt | wc -l > {target}/new.txt')
        os.system(f'cat {target}/old_subdomain.txt | wc -l > {target}/old.txt')

        with open(f'{target}/new.txt', 'r') as file:
            line = file.readline()
            no_new_subdomain = line.strip()
        with open(f'{target}/old.txt', 'r') as file:
            line = file.readline()
            no_old_subdomain = line.strip()
        
        if no_new_subdomain > no_old_subdomain:
            os.system(f'echo "Found New Subdomain For {target}. Check found_new_subdomain.txt" | notify -bulk -id new_subdomain -silent > /dev/null')
            os.system(f'comm -23 <(sort {target}/subdomain.txt) <(sort {target}/old_subdomain.txt) > {target}/found_new_subdomain.txt')
            os.system(f'mv {target}/subdomain.txt {target}/old_subdomain.txt')
        else:
            os.system(f'echo "No New Subdomain For {target}" | notify -bulk -id no_new_subdomain -silent > /dev/null')


Check_Targets()
Check_Old_File(target_list)
Run_Each_Target(target_list)
Check_Newsubdomain(target_list)