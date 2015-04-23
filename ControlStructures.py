"""
code blocks in python are specified using a colon 
and then tabs not curly braces, note: they have to 
be tabs, python actually cares about white space!
In addition, code blocks do not define a new scope
"""

s = "ABCDEF"
while (len(s) > 0):
	l  = 10
	print s
	s = s [1:]
else:
	# you can add an optional else to a loop
	# note: if you break out of loop, the else 
	# will not trigger
	print "loop done!"

# for loop is quite different in pythoin because
# it works with iterators
# generaly syntax is for val in iterable object:

for i in range(0,10,2): # use range for a 'normal' for loop
	print i

# any iterable object works

for c in "Hello":
	print c, # appending a comma prevents a newline 
print

for c in ['H', 'e', 'l', 'l', 'o']:
	print c

for c in ('H', 'e', 'l', 'l', 'o'):
	print c,
print

for i in {"Tom" : 24, "Sally" : 18}.keys():
	print i

for i in {"Tom" : 24, "Sally" : 18}.values():
	print i