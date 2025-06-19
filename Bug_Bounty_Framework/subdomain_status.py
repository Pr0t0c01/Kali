import os
import subprocess
import sys

def Subdomain_Status():
    target = sys.argv[1]
    print(f"[!] Checking Subdomain Status")
    subprocess.run([f'httpx-toolkit -l {target}/subdomain.txt -ports 3000,5000,5001,7000,7474,8000,8001,8008,8080,8081,8088,8090,8091,8333,8443,8880,8888,9000,9001,9043,9090,9091,9100,9200,9443,9800,12443,16080,18091,18092,20720,28017,4433,6443,8009,8082,9040,9300,9990,27017,5984,5601,4000,8089,8800,9443,9080,8010 -mc 200,404,403 -sc -t 30 -o {target}/domains-status.txt'], shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    subprocess.run([f'httpx-toolkit -l {target}/subdomain.txt -ports 80,443,8080,8443,8000 -mc 200,404,403 -sc -t 30 -o {target}/domains-status.txt'], shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    print(f"[+] OK")
    print(f"[!] Split URLs according to Status")
    os.system(f'cat {target}/domains-status.txt | grep "32m200" >> {target}/live-subdomain.txt')
    os.system(f'cat {target}/domains-status.txt | grep "31m403" >> {target}/403-subdomain.txt')
    os.system(f'cat {target}/domains-status.txt | grep "31m404" >> {target}/404-subdomain.txt')
    print(f"[+] OK")
    print(f"[!] Extract URL and Filter Protocols")
    os.system(f'python3 Tools/sorturl.py {target}/live-subdomain.txt {target}/live-subdomain.txt')
    print(f"[+] OK")
    print(f"[!] Add / at the end of line")
    os.system(f'python3 Tools/filter-protocol.py {target}/live-subdomain.txt {target}/live-subdomain.txt')
    print(f"[+] OK")

Subdomain_Status()
