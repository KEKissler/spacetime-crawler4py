import re

def uniqueValidPages():

    numPages = 0

    #read from file, frontier.shelve.urls.txt

    try:
        f = open("frontier.shelve.urls.txt","r",encoding="utf-8",errors="ignore")
        #put into a set()
        urlSet = set()
        line = f.readline()
        entry = line.split(' ')

        while line:
            try:
                if len(entry) > 1 and int(entry[1]) != -1:
                    urlSet.add(entry[0])
            except ValueError:
                pass

            line = f.readline()
            entry = line.split(' ') 

    #return size of set()

    finally:
            f.close()

    numPages = len(urlSet)

    return numPages

#return the number of unique pages
def uniquePages():

    numPages = 0

    #read from file, frontier.shelve.urls.txt

    try:
        f = open("frontier.shelve.urls.txt","r",encoding="utf-8",errors="ignore")
        #put into a set()
        urlSet = set()
        line = f.readline()
        entry = line.split(' ')

        while line:

            urlSet.add(entry[0])
            line = f.readline()
            entry = line.split(' ') 

    #return size of set()

    finally:
        f.close()

    numPages = len(urlSet)

    return numPages


#return the url of the longest page
def maxWordCount():

    maxTokens = 0
    longestPage = ""

    #read from file, frontier.shelve.urls.txt

    try:
        f = open("frontier.shelve.urls.txt","r",encoding="utf-8",errors="ignore")
        line = f.readline()
        entry = line.split(' ')
        longestPage = entry[0]
        maxTokens = int(entry[1])

        while line:

            try:
                if len(entry) > 1 and int(entry[1]) > maxTokens:
                    longestPage = entry[0]
                    maxTokens = int(entry[1])
            except ValueError:
                pass
            line = f.readline()
            entry = line.split(' ')
            

    finally:
        f.close()

    return longestPage


#return a list of the most common words
def mostCommonWords(n):

    try:

        f = open("frontier.shelve.tokens.txt","r",encoding="utf-8")

        #insert into dictionary
        tokens = {}
        line = f.readline().rstrip()

        while line:
        
            if line in tokens:
                tokens[line] += 1
            else:
                tokens[line] = 1

            line = f.readline().rstrip()

        #sort by key-value
        sortedTokenList = sorted(tokens, key = lambda q : (-tokens[q], q))
        result = []
        for x in range(n):
            result.append(sortedTokenList[x])
    
    #copy/print first 50 values

    finally:
        f.close()

    return result





#return list of subdomains, ordered alphabetically with 
#number of unique pages detected in each subdomain
def listSubdomains():

    a = re.compile(r".uci\.edu") 
    
    subDomains = {}


    try:
        f = open("frontier.shelve.urls.txt","r",encoding="utf-8",errors="ignore")
        line = f.readline().rstrip()
        while line: 
            match = re.search(r"(?:[a-zA-Z]+\.)ics\.uci\.edu", line)
            if match is not None:
                subdomain = match[0]
                if len(match.string) > 3 and match.string[:4] == 'www.':
                    subdomain = match.string[4:]
                #print("\t" + match[0])
                if subdomain not in subDomains:
                    subDomains[subdomain] = 1
                else:
                    subDomains[subdomain] += 1

            line = f.readline().rstrip()
            entry = line.split(' ')
        #print(len(subDomains))
        subdomainNames = sorted(subDomains.keys())
        for sd in subdomainNames:
            print(sd + " " + str(subDomains[sd]))
    except:
        print("Ran into an error and left early!")
    finally:
        f.close()
    return None

if __name__ == '__main__':

    print("analysis: ")
    print(uniquePages())
    print(uniqueValidPages())
    print(maxWordCount())

    words = mostCommonWords(50)
    for word in words:
        print(word)
    listSubdomains()


