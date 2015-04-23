""" 
Tuples are immutable ordered collections of arbitrarty objects
Because they are immutable they can be used as dictionary keys
"""
t = ()
print t

t = ('a', 'b', 1, 2, 3.0, "4");
print t
print len(t)

print t[1]
print t[0:3] # first thre items
print t[3:] # fourth item to the end

t2 = ('x', 'x', 'y', 'z')
print t + t2 # concatenate

print t2 * 3 # repeat 3 times

print 'y' in t2
print 'A' in t2

print [x * 2 for x in t2] #comprehension

print t.index("4") 
# print t.index("Abe") throws an exception

print t2.count('x')

t3 = (1, 2, 3, ('a', 'b', 'c', ('D', 'E', 'F'))) # nested tuples
print t3
print len(t3)
print t3[0]
print t3[3]
print t3[3][3]
