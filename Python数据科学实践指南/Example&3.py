
from __future__ import print_function
import csv

with open(path, "r") as f:
	rows = csv.reader(f)

	for row in rows:
		print(row)

with open(path, 'a') as f:
	writer = csv.writer(f)
	writer.writerow(['c1', 'c2', 'c3'])
	for x in range(10):
		writer.writerow([x, chr(ord('a') + x), 'abc'])


with open(path, "r") as f:
	rows = csv.DictReader(f)
	for row in rows:
		print(row)




from __feature__ import print_function
import pandas as pd
from pandas import read_excel

pd.set_option("display.max_columns", 4)
pd.set_option('display.max_rows', 6)

df = read_excel(path, 'sheet1')
print(df)

df = pd.DataFrame([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]], index = [0, 1, 2], columns = list("abcd"))
df.to_excel(path)

