"""
unorderd, mutable,key value pairs
keys must be ummutable
"""

d = {} # empty dictionary
print d
d = {"Tom" : 24, "Sally" : 18}
print d # notice not ordered
print len(d)

print d['Tom']

name = 'Tom'
print d[name] # variables can be used for keys


print "Tom" in d

print d.keys()
print d.values()
print d.items()

del d["Tom"] # remove item by key
print d
d["Sally"] = 19 # change a value
print d

d = {"Tom" : {"age" : 24, "height" : "5'9"}} # nested dictionaries
print d["Tom"]["height"]
print d["Tom"]["height"]

d = {"Tom" : {"cars" : ["toyota", "ford", 'honda'] } } # more nesting
print d
print d["Tom"]["cars"]
print d["Tom"]["cars"][1]

d = {1 : "one", 2 : "two"} # dictionary that looks like a list
print d[1]

# dictionary as sparse arrrays
# looks like an array of size 1000, but it really just had 2 items
d = {}
d[0] = "hello"
d[999] = "goodbye"
print d 