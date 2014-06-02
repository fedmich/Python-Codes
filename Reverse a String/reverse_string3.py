# Reverse a string without using reverse() function
# and using Lambda

s = 'Federico';
li = list( s )	#convert string to lists

ret = [ li[i-1] for i in xrange(len(li),0,-1)  ]	#1 liner lambda
print ( "".join( ret ) )
