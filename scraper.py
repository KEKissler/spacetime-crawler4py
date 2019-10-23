import re
import lxml.html as lxml
from lxml import etree
from urllib.parse import urlparse
from io import StringIO, BytesIO

def scraper(url, resp):
    links = extract_next_links(url, resp)
    return [link for link in links if is_valid(link)]

def extract_next_links(url, resp):
    # Implementation requred.
	print("hi\n")
	print(url, "\n")
	print(resp.url, "\n")
	print(resp.status, "\n")
	print(resp.error, "\n")
	print("*** RAW RESPONSE***")
	print(type(resp.raw_response.content), "\n")
	s = lxml.parse(StringIO(resp.url))
	print(type(s))
	print(s,"\n")

	broke_html = "<html><head><title>test<body><h1>page title</h3>"
	parser = etree.HTMLParser()
	tree = etree.parse(StringIO(broke_html), parser)
	result = etree.tostring(tree.getroot(), pretty_print=True, method="html")
	print(result)

	print(resp.raw_response.content)


	return list()
	
def is_valid(url):
    try:
        parsed = urlparse(url)
        if parsed.scheme not in set(["http", "https"]):
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