import math

def removeAll(l, v):	
	ret = []
	for i in l:
		if i != v:
			ret.append(i)
	return ret

def countAll(l, v):	
	count = 0
	for i in l:
		if i == v:
			count = count + 1
	return count

def distance(p1, p2):	
	dist = math.sqrt( math.pow(p1[0]-p2[0], 2) + math.pow(p1[1]-p2[1], 2) )
	return dist


# global variables
b = 50
c = 100;

def main():
	print removeAll([1,2,3,3,3,3,4], 3)
	print removeAll("ABBBBC", "B")

	print countAll([1,2,3,3,3,3,4], 3)
	print countAll("ABBBBC", "B")

	print distance((0,0), (1,1))
	print distance([0,0], [1,1])

	# b is a local variable, it does not refer to the global b
	b = 800
	print 'locla b ' + str(b)

	# global prevents the creation of a new local variable called c
	# changes to c now change the global variable
	global c
	c = 500


print 'global c before the change ' + str(c)
main()
print 'global c after the change ' + str(c)
print 'global b did not change ' + str(b)