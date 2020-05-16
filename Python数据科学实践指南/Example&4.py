

" abcde\n".strip()
"abcde".capitalize()
"ABCDE".lower()
"abcde".upper()
"abcde figh".title()
"abcde123".isalnum()
"abcde".isdigit()

"abcde".startswith()
"abcde".endswith()

"abcde".index('bc')
"abcde".replace('bc', 'fg')


"{first} is as {second}.".format(first = name, second = 'zhangheng')


from __future__ import print_function
import re
p = re.compile('"(https?://.*?)"', re.I)

with open("./", "r") as f:
	doc = f.read()

for item in p.findall(doc):
	print(item)

	