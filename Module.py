count = 0

def evens(l):
	global count
	count = count + 1
	ret = []
	for i in l:
		if i % 2 == 0:
			ret.append(i)
	return ret

