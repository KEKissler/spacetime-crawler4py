import sys
from PartA import tokenize

args = list(sys.argv)[1:]

'''
to construct each set of tokens this runs tokenize for a cost of O(n) and then builds a frozenset out of that iterable also at cost O(n)
To compare sets, this does O(n) work to iterate over one of the sets and O(n) work to hash those n elements and check for conflicts in the other set
Ideally, this would also do O(1) work to identify the smaller set to iterate over, but that wouldnt actually change the big O notation, only the actual execution time
'''
def similarness(a,b):
    setA = frozenset(tokenize(a))
    setB = frozenset(tokenize(b))
    setC = setA & setB
    return setC

if __name__ == "__main__":
        if len(args) > 1:
            commonSet = similarness(args[0],args[1])
            print(len(commonSet))
