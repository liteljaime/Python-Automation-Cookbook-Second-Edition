import argparse
import requests
import logging
import http.client
import re
from urllib.parse import urlparse, urljoin
from bs4 import BeautifulSoup


DEFAULT_PHRASE = 'python'


def process_link(source_link, text):
    logging.info(f'Extracting links from {source_link}')
    parsed_source = urlparse(source_link)
    result = requests.get(source_link)

    page = BeautifulSoup(result.text, 'html.parser')
    search_text(source_link, page, text)

    return get_links(parsed_source, page)


def get_links(parsed_source, page):
    '''Retrieve the links on the page'''
    links = []
    for element in page.find_all('a'):
        link = element.get('href')
        if not link:
            continue
        # Avoid internal, same page links
        if link.startswith('#'):
            continue

        if link.startswith('mailto:'):
            # Ignore other links like mailto
            # More cases like ftp or similar may be included here
            continue

        # Always accept local links
        if not link.startswith('http'):
            netloc = parsed_source.netloc
            scheme = parsed_source.scheme
            path = parsed_source.path
            link = f'{scheme}://{netloc}{path}'

        # Only parse links in the same domain
        if parsed_source.netloc not in link:
            continue

        links.append(link)

    return links


def search_text(source_link, page, text):
    '''Search for an element with the searched text and print it'''
    for element in page.find_all(text=re.compile(text, flags=re.IGNORECASE)):
        print(
            f'This link {source_link}: --> has the following text: {element}')
