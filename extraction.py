from firecrawl import FirecrawlApp
from pydantic import BaseModel, Field
import os

from dotenv import load_dotenv
load_dotenv()

app = FirecrawlApp(api_key=os.getenv('FIRECRAWL_API_KEY'))
