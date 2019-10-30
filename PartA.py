import sys
import re

args = list(sys.argv)[1:]

'''
Tokenize opens a file, reads it line by line, and remembers any tokens found
it'll get to every line of the file so it'll eventually read it all
The operation of reading every character in a file, line by line or otherwise is O(n)
two regex pattern matches occur on every input,
one replaces specific characters with the empty character, so that is O(n) as it only needs to scan input once to work
the other finds all consecutive word and digit characters in the input and returns those. Again this is O(n) as it only needs to scan input once to work
'''
def tokenize(filePath: str):
    wordPattern = re.compile(r"[\da-z]+", re.MULTILINE | re.IGNORECASE)
    ignoredPunctuation = re.compile(r"[^a-z\s-]", re.IGNORECASE)
    tokens = []
    try:
        file = open(filePath, "r", encoding = "utf-8", errors = "ignore")
        try:
            nextLine = file.readline()
        except:
            nextLine = ""
        #reading one line at a time to be friendly to bigger files
        while nextLine:
            nextLine = re.sub(ignoredPunctuation, '', nextLine)
            for token in re.findall(wordPattern, nextLine):
                tokens.append(str.lower(token))
            try:
                nextLine = file.readline()
            except:
                nextLine = ""
    finally:
        file.close()
    return tokens

'''
ComputeWordFrequencies takes a list of tokens and turns them into a dictionary where the keys are a set of the tokens and the values are their corresponding frequency
Because dictionaries are using hashing, an O(1) operation, n hashes to check if a new token has already been inserted costs a total of O(n)
by the same reasoning, the cost of n additions to the dictionary also costs O(n) as an insertion of a new key pair element is O(1)
'''
def computeWordFrequencies(tokens: [str]):
    tokenMap = {}
    for token in tokens:
        if token in tokenMap:
            tokenMap[token] += 1
        else:
            tokenMap[token] = 1
    return tokenMap

'''
print involves a sort, sorts cost O(n log n)
print on an iterable does O(n) work to iterate over the iterable and print each element
'''
def display(tokenMap:{str:int}):
    for x in sorted(tokenMap.items(), key = lambda a: (-a[1], a[0])):
          print(x[1])

if __name__ == "__main__":
    if len(args) > 0:
        display(computeWordFrequencies(tokenize(args[0])))
