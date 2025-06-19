from random_useragents import get_random_user_agent
from queue import Queue
import requests # type: ignore
import re
import threading
import random
import sys

# Usage
# python3 extract-firebase.py <inputfile> <thread-no> <outputfile>

url_list = sys.argv[1]
thread_no = sys.argv[2]
output_file = sys.argv[3]

# Thread-safe queue
url_queue = Queue()

# Lock for printing safely from threads
print_lock = threading.Lock()

# Regex to extract Firebase projectId
project_id_regex = re.compile(r'(?:["\']?projectId["\']?)\s*[:=]\s*["\'](.*?)["\']', re.IGNORECASE)

print(f'Input - {url_list}, Thread - {thread_no}, Output - {output_file}\n')

def fetch_and_extract():
    while not url_queue.empty():
        url = url_queue.get()

        try:
            headers = {
                "User-Agent": get_random_user_agent()
            }
            response = requests.get(url, headers=headers, timeout=60)
            matches = project_id_regex.findall(response.text)

            with print_lock:
                if matches:
                    print(f"[+] {url} → projectId: {matches[0]}")
                    with open(output_file, "a") as file:
                        file.write(matches[0]+".firebaseio.com\n")
                else:
                    print(f"[-] {url} → No projectId found")

        except Exception as e:
            with print_lock:
                print(f"[!] {url} → Error")
        finally:
            url_queue.task_done()

def main():
    with open(url_list, 'r') as file:
        urls = [line.strip() for line in file if line.strip()]
    
    for url in urls:
        if not url.startswith("http"):
            url = "http://" + url
        url_queue.put(url)

    threads = []
    for _ in range(int(thread_no)):
        thread = threading.Thread(target=fetch_and_extract)
        thread.start()
        threads.append(thread)

    url_queue.join()

if __name__ == "__main__":
    main()