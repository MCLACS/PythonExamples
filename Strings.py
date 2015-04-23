"""
Strings are immutable
"""

s = "Tom"
s = 'Tom' # single or double quotes, single are easier to type
print s

print len(s)
print s[0]

print s[-2] # prints the second to last character
print s[1:3] # prints index 1 and 2, but not 3
print s[:2] # prints the first and second item same as [0:2] 
print s[1:] # prints the second an third item same as [1:3] 

s = "Tom" + "my" # contatenation
print s
s = s * 2 # reptetiion
print s

# s[0] = "x" will not work, immutable

l = list(s) # convert to list
print l
print ''.join(l) # back to a list
print 'X'.join(l) # back to a list w delimeter

print s.find("o") 
print s.find("P")
print s.replace("To", "AB") # does not change the string!
print s.upper()

print '%s is happy, right %s?' % (s, s.upper()) # formatting








