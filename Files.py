for line in open("names.txt", 'r'): # file iterators
	# notice that the new line is read as part of the line
	# and the last line may not have a newline
	print line 

output = open("names2.txt", 'w')
for line in open("names.txt", 'r'):
	line = line.strip("\n") # strip removes character from beg and end
	lst = list(line)
	lst.reverse()
	line = ''.join(lst)
	output.write(line+"\n")

input = open("names.txt", 'r')
lst = input.readlines()
lst.sort()  
# careful, after we sort the item without a newline may be in the middle
# of the list, so just ensure that they all end with one newline
[x.split("\n") for x in lst]
[x+'\n' for x in lst]

output = open("sortedNames.txt", 'w')
output.writelines(lst);
