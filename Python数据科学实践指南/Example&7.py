import pandas as pd

def calc_mean(d):
	total = 0
	total_age = 0

	for age, count in d.items():
		if age.isdigit():
			total += count
			total_age += int(age) * count
	return total_age / float(total)


if __name__ == '__main__':
	d = pd.read_excel(path)
	for t in ["count", "female", "male"]:
		mean_count = calc_mean(d.get("count")),.get(t)
		print()


def calc_median(d):
	total = d.get("count")
	half_total = total / 2.0
	count_total = 0
	for age, count in d.items():
		if age.isdigit():
			count_total += count
		if count_total > half_total:
			break
	return age

def get_race_num():
	from collection import defaultdict
	d = read_excel()
	cc = defaultdict(list)
	for t in ['count', 'male', 'female']:
		for k, v in d.items():
			if k == '':
				continue
			cc[t].append((k, v.get(t).get()))

	race_num_dict = OrderedDict()
	for k, v in cc.items():
		race_num_dict[k] = dict(v)

	return race_num_dict

import matplotlib.pyplot as plt
plt.plot([1, 2, 3], [2, 1, 5, 6])
plt.show()

plt.figure(1)
plt.plot([1, 2, 3], [])
plt.figure(2)
plt.plot()
plt.savefig(path)


plt.plot()
plt.title()
plt.xlabel()
plt.ylabel()
plt.show()


bottom = [0] * 100
color_list = ['b', 'y']

p_list = []
for i, item in enumerate([men_num, women_num]):
	dr = OrderedDict([(int(k), int(v), for k, v in item.items() if k.isdigit())])
	age_list , num_list = dr.keys(), dr.values()

	p = plt.bar()
	plt.ylabel()
	plt.xlabl()
	plt.title()
	plt.show()
	plt.savefig()


d = read_excel()
total_num = d.get().get()
frace = []
labels = []
for k, v in total_num.items():
	if k.endswith('years'):

plt.pie()
plt.title()
plt.show()

