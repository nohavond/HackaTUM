#!/usr/bin/env python3
"""
API backend for the Hauspals app for homeowners.
This API provides all the necessary data for the frontend,
as well as supports basic OAUTH authentication.
"""

__author__ = "Martin Mackovik, Ondrej Nohava, Alphar Abdugeni, Malaz Tamim"
__version__ = "0.1.0"
__license__ = "MIT"

from typing import Union

import uvicorn
from fastapi import FastAPI, HTTPException, Depends, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import JWTError
from pydantic import BaseModel

from CSolar import CSolar
from CStock import CStock
from CUser import CUser
from api_errors import ApiErrors
from authentication import Authentication
from news_fetcher import NewsFetcher

news_fetcher = NewsFetcher()
app = FastAPI()
authentication = Authentication()
c_solar = CSolar()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

dummy_user = CUser()
dummy_user.generate_data()
dummy_stock = CStock()

FORBIDDEN_EXCEPTION = HTTPException(
    status_code=status.HTTP_403_FORBIDDEN,
    detail="Not enough user permissions."
)


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: Union[str, None] = None


class User(BaseModel):
    username: str


class UserInDB(User):
    id: int
    pwd_hash: str
    pwd_salt: str


async def get_current_user(token: str = Depends(oauth2_scheme)) -> UserInDB:
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = authentication.decode_access_token(token)
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
        token_data = TokenData(username=username)
    except JWTError:
        raise credentials_exception
    err_code, user = authentication.get_user(token_data.username)
    if err_code == authentication.ERR_USR_NOT_FOUND:
        raise credentials_exception
    assert err_code == 0
    result = UserInDB
    result.id = user["id"]
    result.pwd_hash = user["pwd_hash"]
    result.pwd_salt = user["pwd_salt"]
    result.username = username
    return result


@app.post("/token")
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    res = authentication.validate_user(form_data.username, form_data.password)
    if res in (authentication.ERR_USR_NOT_FOUND, authentication.ERR_PWD_INVALID):
        raise HTTPException(status_code=400, detail="Incorrect username or password")
    assert res == 0
    return {"access_token": authentication.create_access_token({"sub": form_data.username}), "token_type": "bearer"}


########################################
#          USER API ENDPOINTS          #
########################################
@app.post("/auth/create_user")
async def create_user(user_name: str, pwd: str):
    authentication.add_user(user_name, pwd)


@app.post("/auth/get_my_info")
async def get_user_info(user: UserInDB = Depends(get_current_user)):
    return {"id": user.id,
            "username": user.username}


########################################
#          NEWS API ENDPOINTS          #
########################################
@app.get("/news/get_news")
async def get_news(user_id: int):
    err_code, res = news_fetcher.get_news_all_rss(user_id)
    if err_code == 1:
        raise HTTPException(406, ApiErrors.ERR_USR_NOT_FOUND)
    return res


@app.post("/news/add_feed")
async def add_feed(user_id: int, rss_feed_url: str):
    # if user.id != user_id:
    #     raise FORBIDDEN_EXCEPTION
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


########################################
#       CALCULATION OF SAVINGS         #
########################################

@app.post("/savings/show_savings")
async def show_savings(period: str):
    if period not in ("year", "month", "week", "day"):
        raise HTTPException(400)
    return {"saved": c_solar.show_savings(period, dummy_user)}


@app.post("/savings/show_prices")
async def show_prices(period: str):
    if period not in ("year", "month", "week", "day"):
        raise HTTPException(400)
    return dummy_stock.get_prices(period)


if __name__ == '__main__':
    uvicorn.run("main:app", reload=True, host="192.168.43.52")
