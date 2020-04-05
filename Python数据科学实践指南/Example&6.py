
tuple_list = zip(['a', 'b', 'c', 'd'], [1] * 4)
d = dict(tuple_list)
print(d)

from collections import Counter
doc = ""
doc = doc.split()
count = Counter(doc)
print(cc)
for k, v in count.most_common():
	print("{} \t {}\n".format(k, v))


doc = {}
for w in doc.split():
	if w in doc:
		doc[w] += 1
	else:
		doc[w] = 1
for k, v in sorted(doc.values()):
	print(k ,v)


from collections import defaultdict
c1 = defaultdict(list)
c1.append(1)


tuple_list = zip(['a', 'b', 'c', 'd'], [1] * 4)
for k, v in OrderedDict(tuple_list).items():
	print(k, v)
