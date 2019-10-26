import re
import lxml.html as lxml
from lxml import etree
from urllib.parse import urlparse
from urllib.parse import urlunparse
from io import StringIO, BytesIO
from bs4 import BeautifulSoup


def scraper(url, resp):

    if resp.status >= 600 and resp.status <= 608:
        #print('resp.status error')
        return list()

    links = extract_next_links(url, resp)
    return [link for link in links if is_valid(link)]

def extract_next_links(url, resp):
#    a = parse_urls(resp.raw_response.content)
    a = list()
    soup = BeautifulSoup(resp.raw_response.content)
    for link in soup.find_all('a'):
        a.append(link.get('href'))
    return a

def parse_urls(html_content):
    urlPattern = re.compile(r"(?:https?:\/\/)?(?:www\.)?(?:(?:[a-zA-Z_]+\.)*(?:ics|cs|informatics|stat)|(?:today))\.uci\.edu(?:\/[a-zA-Z_]+)*(?:\.[a-zA-Z_]+)?(?:\?[a-zA-Z_]+=[^\s\"]+)?(?:#[^\s\"]+)?", re.M)
    result = []
    for url in re.findall(urlPattern, str(html_content)):
        try:
            parsed = urlparse(url)
            result.append(urlunparse(parsed))
        except TypeError:
            print("TypeError for ", parsed)
    return result

def is_valid(url):
    try:
        parsed = urlparse(url)
        if parsed.scheme not in set(["http", "https"]):
            return False
        if(re.match(r".*?wics\.ics\.uci\.edu\/events\/category\/boothing.*", str(parsed.path.lower())) is not None):
            return False
        return not re.match(
            r".*\.(css|js|bmp|gif|jpe?g|ico"
            + r"|png|tiff?|mid|mp2|mp3|mp4"
            + r"|wav|avi|mov|mpeg|ram|m4v|mkv|ogg|ogv|pdf"
            + r"|ps|eps|tex|ppt|pptx|doc|docx|xls|xlsx|names"
            + r"|data|dat|exe|bz2|tar|msi|bin|7z|psd|dmg|iso"
            + r"|epub|dll|cnf|tgz|sha1"
            + r"|thmx|mso|arff|rtf|jar|csv"
            + r"|rm|smil|wmv|swf|wma|zip|rar|gz)$", parsed.path.lower())

    except TypeError:
        print ("TypeError for ", parsed)
        raise
