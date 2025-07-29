import requests
from datetime import datetime
from typing import Union, Literal, List
from mcp.server import FastMCP
from pydantic import Field
from typing import Annotated
from mcp.server.fastmcp import FastMCP
from fastmcp import FastMCP, Context
import os
from dotenv import load_dotenv
load_dotenv()
rapid_api_key = os.getenv("RAPID_API_KEY")

__rapidapi_url__ = 'https://rapidapi.com/cristian.liciu/api/newscafapi'

mcp = FastMCP('newscafapi')

@mcp.tool()
def news_caf_technology_latest(q: Annotated[Union[str, None], Field(description='')] = None) -> dict: 
    '''Read full articles, watch videos, browse thousands of titles and more on theTechnology topic with NewsCaf'''
    url = 'https://newscafapi.p.rapidapi.com/apirapid/news/technology/'
    headers = {'x-rapidapi-host': 'newscafapi.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'q': q,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def news_caf_top_stories(q: Annotated[Union[str, None], Field(description='')] = None) -> dict: 
    '''Comprehensive, up-to-date news coverage, aggregated from sources all over the world by NewsCaf'''
    url = 'https://newscafapi.p.rapidapi.com/apirapid/news/'
    headers = {'x-rapidapi-host': 'newscafapi.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'q': q,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def news_caf_world_latest(q: Annotated[Union[str, None], Field(description='')] = None) -> dict: 
    '''Read full articles, watch videos, browse thousands of titles and more on the World topic with NewsCaf'''
    url = 'https://newscafapi.p.rapidapi.com/apirapid/news/world/'
    headers = {'x-rapidapi-host': 'newscafapi.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'q': q,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def news_caf_autos_latest(q: Annotated[Union[str, None], Field(description='')] = None) -> dict: 
    '''Read full articles, watch videos, browse thousands of titles and more on the Autos topic with NewsCaf'''
    url = 'https://newscafapi.p.rapidapi.com/apirapid/news/autos/'
    headers = {'x-rapidapi-host': 'newscafapi.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'q': q,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def news_caf_health_latest(q: Annotated[Union[str, None], Field(description='')] = None) -> dict: 
    '''Read full articles, watch videos, browse thousands of titles and more on the Health topic with NewsCaf'''
    url = 'https://newscafapi.p.rapidapi.com/apirapid/news/health/'
    headers = {'x-rapidapi-host': 'newscafapi.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'q': q,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def news_caf_science_latest(q: Annotated[Union[str, None], Field(description='')] = None) -> dict: 
    '''Read full articles, watch videos, browse thousands of titles and more on the Science topic with NewsCaf'''
    url = 'https://newscafapi.p.rapidapi.com/apirapid/news/science/'
    headers = {'x-rapidapi-host': 'newscafapi.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'q': q,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def news_caf_sports_latest(q: Annotated[Union[str, None], Field(description='')] = None) -> dict: 
    '''Read full articles, watch videos, browse thousands of titles and more on the Sports topic with NewsCaf'''
    url = 'https://newscafapi.p.rapidapi.com/apirapid/news/sports/'
    headers = {'x-rapidapi-host': 'newscafapi.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'q': q,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def news_caf_entertainment_latest(q: Annotated[Union[str, None], Field(description='')] = None) -> dict: 
    '''Read full articles, watch videos, browse thousands of titles and more on the Entertainment topic with NewsCaf'''
    url = 'https://newscafapi.p.rapidapi.com/apirapid/news/entertainment/'
    headers = {'x-rapidapi-host': 'newscafapi.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'q': q,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def news_caf_business_latest(q: Annotated[Union[str, None], Field(description='')] = None) -> dict: 
    '''Read full articles, watch videos, browse thousands of titles and more on the Business topic with NewsCaf'''
    url = 'https://newscafapi.p.rapidapi.com/apirapid/news/business/'
    headers = {'x-rapidapi-host': 'newscafapi.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'q': q,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()



if __name__ == '__main__':
    import sys
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 9997
    mcp.run(transport="stdio")
