import re
import lxml.html as lxml
from lxml import etree
from urllib.parse import urlparse
from urllib.parse import urlunparse
from io import StringIO, BytesIO
from bs4 import BeautifulSoup


def scraper(url, resp):
    if resp.status >= 400 and resp.status < 600:
        return list()
    if resp.status >= 600 and resp.status <= 608:
        return list()

    links = extract_next_links(url, resp)
    return [link for link in links if is_valid(link)]

def extract_next_links(url, resp):
    a = list()
    #soup = BeautifulSoup(resp.raw_response.content, features="lxml")
    soup = BeautifulSoup(resp.raw_response.text.encode("utf-8"), features="lxml")
    for link in soup.find_all('a'):
        a.append(normalize_link(url, link.get('href')))
    return a

def normalize_link(current_link, new_link):
    parsed = urlparse(new_link)
    parsedOld = urlparse(current_link)
    if(parsed.path != "" and parsed.netloc == ""):
        if(re.match(r"\w+@\w+\.[a-zA-Z]+", parsed.path) is None): #verify path is not an email, so we dont make a lot of bogus email links
            return urlunparse((parsedOld[0], parsedOld[1], parsed[2], parsed[3], parsed[4], ""))
    return urlunparse((parsed[0], parsed[1], parsed[2], parsed[3], parsed[4], ""))


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
            if(re.match(nextLine, str(parsed.geturl())) is not None):
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
            + r"|war|apk|sql|ppsx|pptx)$", parsed.path.lower())

    except TypeError:
        print ("TypeError for ", parsed)
        raise
