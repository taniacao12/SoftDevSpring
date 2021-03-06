import datetime
from functools import reduce

#read Grimm's Fairy Tails
fd = open("fairytail.txt", "r", encoding="utf8" )
lines = fd.read()
lines = " ".join( lines.split("--") )
lines = " ".join( lines.split("\n") )
lines = " ".join( lines.split("\'") )

words = lines.split(" ")
words = [ x.strip( ",.?/!~#$%^&*(){}[];:\'\"" ) for x in words ]

#print( words )

# Find the frequency of a single word
def find_1( word ):
    count_1 = [ 1 for x in words if x == word ]

    return reduce( (lambda x, y: x + y), count_1 )

print( find_1( "fox" ) )
print( find_1( "to" ) )

# Find the total frequency of a group of words
def find_mult( li ):
    count_mult = [ 1 for x in range(len(words)-len(li)+1) \
                       for i in range(len(li)) \
                       if " ".join([ y for y in words[x:len(li)+x] ]) \
                       == " ".join([ y for y in li])]

    if len( count_mult ) == 0:
        return 0
    
    return reduce( (lambda x, y: x + y), count_mult )

print( "finding: fox to -- {}".format( find_mult( ["fox"] ) ) )
print( find_mult( ["and", "the"] ) )

# Find the most frequently occurring word
def findmost():
    print(datetime.datetime.now())
    
    allw=[]
    [allw.append(x) for x in words if x not in allw]

    print(datetime.datetime.now())

    counts = [ [ x, find_1(x) ] for x in allw ]

    print(datetime.datetime.now())

    return reduce( (lambda x, y: x if x[1] >= y[1] else y), counts )

print( findmost() )
