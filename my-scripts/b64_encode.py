#!/usr/bin/python3

import base64
import sys

text = str(sys.argv[1])
text_to_ascii = text.encode("ascii")
ascii_to_base64 = base64.b64encode(text_to_ascii)
base64_to_ascii = ascii_to_base64.decode("ascii")

print(base64_to_ascii)
