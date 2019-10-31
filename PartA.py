import sys
import re

args = list(sys.argv)[1:]
q = {"a",
"about",
"above",
"after",
"again",
"against",
"all",
"am",
"an",
"and",
"any",
"are",
"arent",
"as",
"at",
"be",
"because",
"been",
"before",
"being",
"below",
"between",
"both",
"but",
"by",
"cant",
"cannot",
"could",
"couldnt",
"did",
"didnt",
"do",
"does",
"doesnt",
"doing",
"dont",
"down",
"during",
"each",
"few",
"for",
"from",
"further",
"had",
"hadnt",
"has",
"hasnt",
"have",
"havent",
"having",
"he",
"hed",
"hell",
"hes",
"her",
"here",
"heres",
"hers",
"herself",
"him",
"himself",
"his",
"how",
"hows",
"i",
"id",
"ill",
"im",
"ive",
"if",
"in",
"into",
"is",
"isnt",
"it",
"its",
"its",
"itself",
"lets",
"me",
"more",
"most",
"mustnt",
"my",
"myself",
"no",
"nor",
"not",
"of",
"off",
"on",
"once",
"only",
"or",
"other",
"ought",
"our",
"ours",
"ourselves",
"out",
"over",
"own",
"same",
"shant",
"she",
"shed",
"shell",
"shes",
"should",
"shouldnt",
"so",
"some",
"such",
"than",
"that",
"thats",
"the",
"their",
"theirs",
"them",
"themselves",
"then",
"there",
"theres",
"these",
"they",
"theyd",
"theyll",
"theyre",
"theyve",
"this",
"those",
"through",
"to",
"too",
"under",
"until",
"up",
"very",
"was",
"wasnt",
"we",
"wed",
"well",
"were",
"weve",
"were",
"werent",
"what",
"whats",
"when",
"whens",
"where",
"wheres",
"which",
"while",
"who",
"whos",
"whom",
"why",
"whys",
"with",
"wont",
"would",
"wouldnt",
"you",
"youd",
"youll",
"youre",
"youve",
"your",
"yours",
"yourself",
"yourselves"}

def tokenize(string):
    tokenCount = 0
    wordPattern = re.compile(r"[\da-z]+", re.MULTILINE | re.IGNORECASE)
    ignoredPunctuation = re.compile(r"[^a-z\s-]", re.IGNORECASE)
    try:
        tokenFile = open("frontier.shelve.tokens.txt","a+")
        string = re.sub(ignoredPunctuation, '', string)
        for token in re.findall(wordPattern, string):
            if token.strip().lower() not in q:
                tokenCount += 1;
                tokenFile.write(token.lower() + "\n")
    finally:
        tokenFile.close()
    return tokenCount;

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
