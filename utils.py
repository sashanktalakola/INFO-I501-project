from dotenv import load_dotenv
import replicate
import os
import requests
from bs4 import BeautifulSoup

load_dotenv()

def get_article_data(page_url):
    response = requests.get(page_url, headers={"User-Agent": "Mozilla/5.0"})

    if response.status_code == 200:
        page_content = response.text
        soup = BeautifulSoup(page_content, 'html.parser')
        paragraphs = soup.find_all('p')

        paragraphs = [paragraph.text for paragraph in paragraphs]
        paragraphs = list(map(str.strip, paragraphs))

        try:
            share_paragraph_index = paragraphs.index("Share")
            paragraphs = paragraphs[share_paragraph_index+1:]

            page_footer_index = paragraphs.index("--")
            paragraphs = paragraphs[:page_footer_index]
        except:
            pass
        all_paragraphs = " ".join(paragraphs)

        return all_paragraphs
    else:
        return -1