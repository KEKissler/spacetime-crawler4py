import sys
import re

args = list(sys.argv)[1:]
q = {"a","a's","able","about","above","according","accordingly","across","actually","after","afterwards","again","against","ain't","all","allow","allows","almost","alone","along","already","also","although","always","am","among","amongst","an","and","another","any","anybody","anyhow","anyone","anything","anyway","anyways","anywhere","apart","appear","appreciate","appropriate","are","aren't","around","as","aside","ask","asking","associated","at","available","away","awfully","b","be","became","because","become","becomes","becoming","been","before","beforehand","behind","being","believe","below","beside","besides","best","better","between","beyond","both","brief","but","by","c","c'mon","c's","came","can","can't","cannot","cant","cause","causes","certain","certainly","changes","clearly","co","com","come","comes","concerning","consequently","consider","considering","contain","containing","contains","corresponding","could","couldn't","course","currently","d","definitely","described","despite","did","didn't","different","do","does","doesn't","doing","don't","done","down","downwards","during","e","each","edu","eg","eight","either","else","elsewhere","enough","entirely","especially","et","etc","even","ever","every","everybody","everyone","everything","everywhere","ex","exactly","example","except","f","far","few","fifth","first","five","followed","following","follows","for","former","formerly","forth","four","from","further","furthermore","g","get","gets","getting","given","gives","go","goes","going","gone","got","gotten","greetings","h","had","hadn't","happens","hardly","has","hasn't","have","haven't","having","he","he's","hello","help","hence","her","here","here's","hereafter","hereby","herein","hereupon","hers","herself","hi","him","himself","his","hither","hopefully","how","howbeit","however","i","i'd","i'll","i'm","i've","ie","if","ignored","immediate","in","inasmuch","inc","indeed","indicate","indicated","indicates","inner","insofar","instead","into","inward","is","isn't","it","it'd","it'll","it's","its","itself","j","just","k","keep","keeps","kept","know","known","knows","l","last","lately","later","latter","latterly","least","less","lest","let","let's","like","liked","likely","little","look","looking","looks","ltd","m","mainly","many","may","maybe","me","mean","meanwhile","merely","might","more","moreover","most","mostly","much","must","my","myself","n","name","namely","nd","near","nearly","necessary","need","needs","neither","never","nevertheless","new","next","nine","no","nobody","non","none","noone","nor","normally","not","nothing","novel","now","nowhere","o","obviously","of","off","often","oh","ok","okay","old","on","once","one","ones","only","onto","or","other","others","otherwise","ought","our","ours","ourselves","out","outside","over","overall","own","p","particular","particularly","per","perhaps","placed","please","plus","possible","presumably","probably","provides","q","que","quite","qv","r","rather","rd","re","really","reasonably","regarding","regardless","regards","relatively","respectively","right","s","said","same","saw","say","saying","says","second","secondly","see","seeing","seem","seemed","seeming","seems","seen","self","selves","sensible","sent","serious","seriously","seven","several","shall","she","should","shouldn't","since","six","so","some","somebody","somehow","someone","something","sometime","sometimes","somewhat","somewhere","soon","sorry","specified","specify","specifying","still","sub","such","sup","sure","t","t's","take","taken","tell","tends","th","than","thank","thanks","thanx","that","that's","thats","the","their","theirs","them","themselves","then","thence","there","there's","thereafter","thereby","therefore","therein","theres","thereupon","these","they","they'd","they'll","they're","they've","think","third","this","thorough","thoroughly","those","though","three","through","throughout","thru","thus","to","together","too","took","toward","towards","tried","tries","truly","try","trying","twice","two","u","un","under","unfortunately","unless","unlikely","until","unto","up","upon","us","use","used","useful","uses","using","usually","uucp","v","value","various","very","via","viz","vs","w","want","wants","was","wasn't","way","we","we'd","we'll","we're","we've","welcome","well","went","were","weren't","what","what's","whatever","when","whence","whenever","where","where's","whereafter","whereas","whereby","wherein","whereupon","wherever","whether","which","while","whither","who","who's","whoever","whole","whom","whose","why","will","willing","wish","with","within","without","won't","wonder","would","wouldn't","x","y","yes","yet","you","you'd","you'll","you're","you've","your","yours","yourself","yourselves","z","zero"}
'''
Tokenize opens a file, reads it line by line, and remembers any tokens found
it'll get to every line of the file so it'll eventually read it all
The operation of reading every character in a file, line by line or otherwise is O(n)
two regex pattern matches occur on every input,
one replaces specific characters with the empty character, so that is O(n) as it only needs to scan input once to work
the other finds all consecutive word and digit characters in the input and returns those. Again this is O(n) as it only needs to scan input once to work
'''

def tokenize(string):
    stopwordSet = None
    string = ""
    try:
        for x in open("soupSiteText.txt", "r", encoding = "utf-8").readlines():
            string += x
        file = open("stop_words.txt", "r", encoding = "utf-8")
        wordList = []
        nextLine = file.readline()
        while nextLine:
            wordList.append(nextLine)
            nextLine = file.readline()
        stopwordSet = set(wordList)
    finally:
        file.close()
    print(len(stopwordSet))
        
    tokenCount = 0
    wordPattern = re.compile(r"[\da-z]+", re.MULTILINE | re.IGNORECASE)
    ignoredPunctuation = re.compile(r"[^a-z\s-]", re.IGNORECASE)
    try:
        tokenFile = open("tokens.txt","a+")
        string = re.sub(ignoredPunctuation, '', string)
        for token in re.findall(wordPattern, string):
            if token.strip().lower() not in q:
                print(token)
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
