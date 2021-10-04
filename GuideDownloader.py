from urllib import parse
import requests
from bs4 import BeautifulSoup

request_headers = {"user-agent": "Mozilla/5.0 (iPad; U; CPU OS 3_2_1 like Mac OS X; en-us) AppleWebKit/531.21.10 (KHTML, like Gecko) Mobile/7B405"}

class GuideContent:
    def __init__(self, content, is_textguide):
        self.content = content
        self.is_textguide = is_textguide

def is_remote_url(url):
    decomposed_url = parse.urlparse(url)
    return decomposed_url.scheme in ["http" ,"https"]

def download_guide(url):
    response = requests.Session().get(url, headers=request_headers)

    # Check if guide is a pure text document (URL usually ends in .txt)
    if "text/plain" in response.headers["Content-type"]:
        content = response.text
        lines = content.splitlines(keepends=True)
        return GuideContent(lines, True)
    # If not pure text, then treat as HTML
    else:
        soup = BeautifulSoup(response.text, features="html.parser")
        content = soup.select_one(".faqtext")
        # Guide is a text-based (as opposed to new HTML guides)
        is_textguide = content != None
        if(is_textguide):
            lines = content.text.splitlines(keepends=True)
            return GuideContent(lines, True)
        else:
            # Implement HTML guide parsing
            return GuideContent([], False)

