def print_differing(ratio):
	for k in dictlist[0]:
		v1 = dictlist[0][k]
		v2 = dictlist[1][k]
		v3 = dictlist[2][k] 
		if (v1/v2 > ratio or v1/v3 > ratio or v2/v1 > ratio or v2/v3 > ratio or v3/v1 > ratio or v3/v2 > ratio):
			print(k, ":\t", dictlist[0][k], dictlist[1][k], dictlist[2][k])


def print_avg():
	for k in dictlist[0]:
		print(k, "\t", dictlist[0][k], dictlist[1][k], dictlist[2][k])


dictlist = [dict() for x in range (3)]
avg = [0,0,0]

for i in range(3):
	filename = "data/" + str(i+1) + ".txt"
	f = open(filename, 'r')
	for line in f:
		name, value = line.split()
		avg[i] += float(value)/6
		dictlist[i][name] = dictlist[i].get(name, 0) + float(value)/6
	avg[i] /= len(dictlist[i])

print_differing(1.45)
