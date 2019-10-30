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
"aren't",
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
"can't",
"cannot",
"could",
"couldn't",
"did",
"didn't",
"do",
"does",
"doesn't",
"doing",
"don't",
"down",
"during",
"each",
"few",
"for",
"from",
"further",
"had",
"hadn't",
"has",
"hasn't",
"have",
"haven't",
"having",
"he",
"he'd",
"he'll",
"he's",
"her",
"here",
"here's",
"hers",
"herself",
"him",
"himself",
"his",
"how",
"how's",
"i",
"i'd",
"i'll",
"i'm",
"i've",
"if",
"in",
"into",
"is",
"isn't",
"it",
"it's",
"its",
"itself",
"let's",
"me",
"more",
"most",
"mustn't",
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
"shan't",
"she",
"she'd",
"she'll",
"she's",
"should",
"shouldn't",
"so",
"some",
"such",
"than",
"that",
"that's",
"the",
"their",
"theirs",
"them",
"themselves",
"then",
"there",
"there's",
"these",
"they",
"they'd",
"they'll",
"they're",
"they've",
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
"wasn't",
"we",
"we'd",
"we'll",
"we're",
"we've",
"were",
"weren't",
"what",
"what's",
"when",
"when's",
"where",
"where's",
"which",
"while",
"who",
"who's",
"whom",
"why",
"why's",
"with",
"won't",
"would",
"wouldn't",
"you",
"you'd",
"you'll",
"you're",
"you've",
"your",
"yours",
"yourself",
"yourselves"}

def tokenize(string):
    string = ""
    try:
        for x in open("soupSiteText.txt", "r", encoding = "utf-8").readlines():
            string += x
    finally:
        file.close()
        
    tokenCount = 0
    wordPattern = re.compile(r"[\da-z]+", re.MULTILINE | re.IGNORECASE)
    ignoredPunctuation = re.compile(r"[^a-z\s-]", re.IGNORECASE)
    try:
        tokenFile = open("tokens.txt","a+")
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
