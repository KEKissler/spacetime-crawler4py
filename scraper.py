import re
from os.path import normpath
import lxml.html as lxml
from lxml import etree
from urllib.parse import urlparse
from urllib.parse import urlunparse
from urllib.parse import urljoin
from Tokenize import tokenize
from io import StringIO, BytesIO
from bs4 import BeautifulSoup

def scraper(url, resp):
    if resp.status >= 400 and resp.status < 600:
        return list()
    if resp.status >= 600 and resp.status <= 608:
        return list()
    if resp.status == 200 and resp.raw_response is None:
        return list()
    soup = BeautifulSoup(resp.raw_response.content, features="lxml")
    links = extract_next_links(url, soup)
    contentText = ""
    for contentGroup in soup.find_all(['p', 'title', re.compile(r"^h[0-9]+$")]):
        for string in contentGroup.stripped_strings:
            contentText += string + ' '
    try:
        urlsFile = open("frontier.shelve.urls.txt","a+", encoding = "utf-8")
        urlsFile.write(str(url) + " " + str(tokenize(contentText)) + '\n')
        result = []
        for link in links:
            if is_valid(link):
                result.append(link)
            else:
                urlsFile.write(str(link) + " -1\n")
    finally:
        urlsFile.close()

    return result;

def extract_next_links(url, soup):
    return [remove_fragment(urljoin(url, link.get('href'))) for link in soup.find_all('a')]

def remove_fragment(url):
    parsed = urlparse(url)
    return urlunparse((parsed[0], parsed[1], parsed[2], parsed[3], parsed[4], ""))
'''
def normalize_link(current_link, new_link):
    print("\t\tProcessingLink: " + new_link)
    parsed = urlparse(new_link)
    parsedOld = urlparse(current_link)
    if(parsed.path != "" and parsed.netloc == ""):
        print("\trelative link found with path: " +  parsed.path + "\n\t" + "netloc is: " + parsed.netloc)
        if(re.match(r"@+", parsed.path) is None): #verify path is not an email, so we dont make a lot of bogus email links
            newPath = parsedOld[2]
            try:
                newPath = newPath[:newPath.rfind(r'/')]
            except ValueError:
                newPath = ""
            newPath += parsed[2]
            newPath = normpath(newPath)
            newPath = re.sub(r"\\", '/', normpath(newPath))
            return urlunparse((parsedOld[0], parsedOld[1], newPath, parsed[3], parsed[4], ""))
    return urlunparse((parsed[0], parsed[1], parsed[2], parsed[3], parsed[4], ""))
'''

def is_valid(url):
    try:
        parsed = urlparse(url)
        if parsed.scheme not in set(["http", "https"]):
            return False
        if(re.match(r".*?((^|\.)(ics|cs|informatics|stat)\.uci\.edu)|(today\.uci\.edu\/department\/information_computer_sciences).*", parsed.netloc) is None):
            return False
        if(re.match(r"[^\w:\/%@\.\&\-_\?,= ]", parsed.geturl()) is not None):
            print("CONTAINS INVALID CHARACTERS: " + parse.geturl())
            return False
        file = open("blacklist.txt", "r", encoding = "utf-8", errors = "ignore")
        nextLine = file.readline()
        while nextLine:
            if(re.match(nextLine.strip(), str(parsed.geturl())) is not None):
                print("Ignored " + parsed.geturl() + " due to blacklist line" + nextLine)
                return False
            nextLine = file.readline()
        file.close()
        return not re.match(
            r".*\.(css|js|bmp|gif|jpe?g|ico"
            + r"|png|tiff?|mid|mp2|mp3|mp4"
            + r"|wav|avi|mov|mpeg|ram|m4v|mkv|ogg|ogv|pdf"
            + r"|ps|eps|tex|ppt|pptx|doc|docx|xls|xlsx|names"
            + r"|data|dat|exe|bz2|tar|msi|bin|7z|psd|dmg|iso"
            + r"|epub|dll|cnf|tgz|sha1"
            + r"|thmx|mso|arff|rtf|jar|csv"
            + r"|rm|smil|wmv|swf|wma|zip|rar|gz"
	    + r"|pdf|pdfs|css|js|ppts|exe|o"
            + r"|tvs|bgz|tbi|bib|m|odc|pps"
            + r"|war|apk|sql|ppsx|pptx)$", parsed.path.lower())

    except TypeError:
        print ("TypeError for ", parsed)
        raise
