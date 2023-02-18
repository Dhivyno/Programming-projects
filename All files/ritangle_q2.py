start = [1, 2, 3, 4, 5, 6, 7, 8, 9]
first = []
second = []
third = []
fourth = []
fifth = []
sixth = []
seventh = []
eighth = []
test = []
test2 = []
for j in range(len(start)):
	for i in range(0, 10):
		if (start[j]*10+i) % 2 == 0:
			first.append((start[j]*10+i))

for j in range(len(first)):
	for i in range(0, 10):
		if (first[j]*10+i) % 3 == 0:
			second.append((first[j]*10+i))

for j in range(len(second)):
	for i in range(0, 10):
		if (second[j]*10+i) % 4 == 0:
			third.append((second[j]*10+i))

for j in range(len(third)):
	for i in range(0, 10):
		if (third[j]*10+i) %  5 == 0:
			fourth.append((third[j]*10+i))

for j in range(len(fourth)):
	for i in range(0, 10):
		if (fourth[j]*10+i) % 6 == 0:
			fifth.append((fourth[j]*10+i))

for j in range(len(fifth)):
	for i in range(0, 10):
		if (fifth[j]*10+i) % 7 == 0:
			sixth.append((fifth[j]*10+i))

for j in range(len(sixth)):
	for i in range(0, 10):
		if (sixth[j]*10+i) % 8 == 0:
			seventh.append((sixth[j]*10+i))

for j in range(len(seventh)):
	for i in range(0, 10):
		if (seventh[j]*10+i) % 9 == 0:
			eighth.append((seventh[j]*10+i))

for i in range(len(eighth)):
	randomvar = 0
	for j in range(len(str(eighth[i]))):
		for k in range(len(str(eighth[i]))):
			if j == k:
				continue
			elif str(eighth[i])[j] == str(eighth[i])[k]:
				randomvar = 1
	if randomvar == 0:
		print(str(eighth[i])+"0")


