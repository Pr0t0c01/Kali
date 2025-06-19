#!/usr/bin/python3

import base64
import sys

base64_text = str(sys.argv[1])
base64_to_ascii = base64_text.encode("ascii")
base64_decoding = base64.b64decode(base64_to_ascii)
text = base64_decoding.decode("ascii")

print(text)