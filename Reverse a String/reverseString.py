#This code runs for Python 3.4.2

import sys
import timeit

def reverseWordSlice(word):
    #Reverse usign slice notation
    #Slices work as follows:
    #seq[:]                # [seq[0],   seq[1],          ..., seq[-1]    ]
    #seq[low:]             # [seq[low], seq[low+1],      ..., seq[-1]    ]
    #seq[:high]            # [seq[0],   seq[1],          ..., seq[high-1]]
    #seq[low:high]         # [seq[low], seq[low+1],      ..., seq[high-1]]
    #seq[::stride]         # [seq[0],   seq[stride],     ..., seq[-1]    ]
    #seq[low::stride]      # [seq[low], seq[low+stride], ..., seq[-1]    ]
    #seq[:high:stride]     # [seq[0],   seq[stride],     ..., seq[high-1]]
    #seq[low:high:stride]  # [seq[low], seq[low+stride], ..., seq[high-1]]
    # +---+---+---+---+---+
    #  | H | o | l | a | ! |
    #  +---+---+---+---+---+
    #  0   1   2   3   4   5
    # -5  -4  -3  -2  -1
    return word[::-1]

def reverseWordArray(word):
    # Reverse a string with reverse() function
    array = []
    for letter in word:
        array.append( letter )
    array.reverse()
    return ("".join(array))

def reverseWordArrayNoob(word):
    # Reverse a string without using reverse() function
    array = []

    length = len(word)
    for i in range(length,0,-1):
        array.append(word[ i - 1])

    return ("".join(array))

def reverseWordLambda(word):
    # Using Lambda

    li = list(word)

    ret = [li[i-1] for i in range(len(li),0,-1)]
    return ("".join(ret))

time = str(timeit.timeit(reverseWordSlice(sys.argv[1])))
reversedValue = reverseWordSlice(sys.argv[1])
print('Time ' + time + ' Value ' + reversedValue + 'reverseWordSlice')

time = str(timeit.timeit(reverseWordArray(sys.argv[1])))
reversedValue = reverseWordArray(sys.argv[1])
print('Time ' + time + ' Value ' + reversedValue + 'reverseWordArray')

time = str(timeit.timeit(reverseWordArrayNoob(sys.argv[1])))
reversedValue = reverseWordArrayNoob(sys.argv[1])
print('Time ' + time + ' Value ' + reversedValue + 'reverseWordArrayNoob')

time = str(timeit.timeit(reverseWordLambda(sys.argv[1])))
reversedValue = reverseWordLambda(sys.argv[1])
print('Time ' + time + ' Value ' + reversedValue + 'reverseWordLambda')