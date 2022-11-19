#!/usr/bin/env python3
"""
API backend for the Hauspals app for homeowners.
This API provides all the necessary data for the frontend,
as well as supports basic OAUTH authentication.
"""

__author__ = "Martin Mackovik, Ondrej Nohava, Alphar Abdugeni, Malaz Tamim"
__version__ = "0.1.0"
__license__ = "MIT"

from fastapi import FastAPI
import argparse

app = FastAPI()


@app.get("/")
async def root():
    return {"Message": "Hello world!"}


@app.get("/news/get_news")
async def get_news():
    return {"articles": [
        {"title": "Title of an article",
         "description": "Short description of an article",
         "long_text": "Long text of an article"}
    ]}


@app.post("/news/add_feed")
async def add_feed():
    return {}


@app.post("/news/remove_feed")
async def remove_feed():
    return {}


@app.post("/news/get_feeds_list")
async def get_feeds():
    return {}
