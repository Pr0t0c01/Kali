
#!/usr/bin/env python3

import re
import sys

def uuid_grep():
    uuid_regex = re.compile(r'[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}')
    for line in sys.stdin:
        match = uuid_regex.search(line)
        if match:
            print(match.group(0))

if __name__ == "__main__":
    uuid_grep()