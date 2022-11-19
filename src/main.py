#!/usr/bin/env python3
"""
API backend for the Hauspals app for homeowners.
This API provides all the necessary data for the frontend,
as well as supports basic OAUTH authentication.
"""

__author__ = "Martin Mackovik, Ondrej Nohava, Alphar Abdugeni, Malaz Tamim"
__version__ = "0.1.0"
__license__ = "MIT"

import uvicorn
from fastapi import FastAPI, HTTPException
from news_fetcher import NewsFetcher
from api_errors import ApiErrors

news_fetcher = NewsFetcher()
app = FastAPI()


@app.get("/news/get_news")
async def get_news(user_id: int):
    err_code, res = news_fetcher.get_news_all_rss(user_id)
    if err_code == 1:
        raise HTTPException(406, ApiErrors.ERR_USR_NOT_FOUND)
    return res


@app.post("/news/add_feed")
async def add_feed(user_id: int, rss_feed_url: str):
    err_code, res = news_fetcher.add_rss_feed(user_id, rss_feed_url)
    assert err_code == 0
    return res


@app.post("/news/remove_feed")
async def remove_feed(user_id: int, rss_feed_id: int):
    err_code = news_fetcher.rm_rss_feed(user_id, rss_feed_id)
    if err_code == 1:
        raise HTTPException(406, ApiErrors.ERR_USR_NOT_FOUND)
    if err_code == 2:
        raise HTTPException(406, ApiErrors.ERR_RSS_FEED_NOT_FOUND)
    return {}


@app.post("/news/get_feeds_list")
async def get_feeds(user_id: int):
    err_code, res = news_fetcher.get_rss_feed_list(user_id)
    if err_code == 1:
        raise HTTPException(406, ApiErrors.ERR_USR_NOT_FOUND)
    return res


if __name__ == '__main__':
    uvicorn.run("main:app", reload=True)
