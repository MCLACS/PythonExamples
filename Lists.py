"""
Lists - ordered, accept different types items, mutable, grows as needed
"""
mylist = [1, "2", 3.0]
print mylist

print len(mylist)
print mylist[1] # 1-based indexing
mylist =  mylist + ["new", "items"] # + appends
print mylist

print mylist[:2] # new list from start up to but not including 3rd item
print mylist[1:3] # new list from item 1 up to but not including 4th item
print mylist[3:] # new list from item 3 to end
print mylist[-1] # last item
print mylist[-2:] # second to last item to end

mylist.pop(2) #delete the third item
print mylist

mylist.insert(2, -99) # insert in third spot
print mylist

mylist.sort()
print mylist

mylist.reverse()
print mylist

print range(4) #ranges
print range(4, 10, 2) #ranges

nested = [ [1,2,3], [4,5,6] ] # lists can nest!
print nested[1][2]

print [x * 2 for x in nested[0]] # comprehension
print [x * 2 for x in range(11)] # comprehension
print [ [x, x * 2] for x in range(11)] # comprehension

l1 = [1, 2, 3]
l2 = l1
l3 = [1, 2, 3]
print l1 == l2
print l1 is l2
print l1 == l3
print l1 is l3

l2.reverse() # all variables are pointers in python
print l1 




