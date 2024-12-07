# Install with pip install firecrawl-py
from firecrawl import FirecrawlApp
import os

from dotenv import load_dotenv
load_dotenv()

app = FirecrawlApp(api_key=os.getenv('FIRECRAWL_API_KEY'))

crawl_result = app.crawl_url(
    'https://paulgraham.com/articles.html',
    params={
        'limit': 100,
        'scrapeOptions': {
            'formats': [ 'markdown', 'html' ],
        },
    },
    poll_interval=30
)

print(crawl_result)