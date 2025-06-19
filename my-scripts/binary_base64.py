import base64

for i in range(101):
	payload = "user"+str(i)
	res = ''.join(format(ord(i), '08b') for i in payload)
	sample_string_bytes = res.encode("ascii")
	base64_bytes = base64.b64encode(sample_string_bytes)
	base64_string = base64_bytes.decode("ascii")
	print(base64_string)
