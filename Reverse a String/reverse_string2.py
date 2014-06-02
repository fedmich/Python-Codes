# Reverse a string without using reverse() function

s = 'Federico';
r = []

length = len(s)
for i in xrange(length,0,-1):
	r.append( s[ i - 1] )

print ( "".join(r) )