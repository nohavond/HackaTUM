import datetime
import time

import feedparser
import uvicorn

ERR_USR_NOT_FOUND = \
    {
        "error": {
            "code": 406,
            "message": "User not found in the RSS feed list"
        }
    }

ERR_RSS_FEED_NOT_FOUND = \
    {
        "error": {
            "code": 406,
            "message": "RSS feed not found for the specific user"
        }
    }


class NewsFetcher:
    """
    Class used for management of RSS feeds list for every user
    and for parsing and returning news from said RSS feeds.
    """

    def __init__(self):
        self.tmp_feed_list = dict()
        self.cached_feeds = dict()
        self.tmp_feed_list[0] = [{"feed_id": 0,
                                  "feed_url": "https://search.cnbc.com/rs/search/combinedcms/view.xml?partnerId=wrss01&id=10000115"}]

    def _get_news_single_rss(self, rss_feed: str):
        """
        Fetches the news from the selected RSS, either from local cache
        or from the URL if the cache is too old.
        :param rss_feed: URL of the RSS feed to fetch
        :return: List of articles of said RSS feed
        """
        is_cached = rss_feed in self.cached_feeds.keys()
        if is_cached:
            cached_feed = self.cached_feeds[rss_feed]
            update_time_delta = datetime.datetime.now().timestamp() - cached_feed["last_update"]
            if update_time_delta < 10 * 60:
                return cached_feed["articles"]
        parsed: feedparser.FeedParserDict = feedparser.parse(rss_feed)
        result = []
        for entry in parsed.entries[:10]:
            article = {
                "title": entry["title"],
                "description": entry["description"],
                "utc": time.mktime(entry["published_parsed"])
            }
            result.append(article)
        self.cached_feeds[rss_feed] = \
            {
                "last_update": datetime.datetime.now().timestamp(),
                "articles": result
            }
        return result

    def _get_next_rss_id(self, user_id: int):
        """
        Returns the next free ID of RSS feed for the specified user.
        :param user_id: ID of user to find free RSS id for.
        :return: Free RSS feed id fot the specified user
        """
        if user_id not in self.tmp_feed_list.keys():
            return 0, 0
        rss_feeds = self.get_rss_feed_list(user_id)
        ids = [rss_feed['feed_id'] for rss_feed in rss_feeds[1]['rss_feed_list']]
        return 0, max(ids) + 1

    def get_news_all_rss(self, user_id: int):
        """
        Fetches all the news from the specified users' all RSS feeds.
        :param user_id: ID of users to fetch news for
        :return: List of articles of all RSS feeds
        """
        err_code, rss_feeds = self.get_rss_feed_list(user_id)
        if err_code != 0:
            return err_code, {}
        all_articles = []
        for feed in rss_feeds["rss_feed_list"]:
            all_articles += self._get_news_single_rss(feed["feed_url"])
        all_articles.sort(key=lambda x: x["utc"], reverse=True)
        return 0, all_articles

    def get_rss_feed_list(self, user_id: int):
        """
        Returns the list of RSS feeds for the specified user.
        :param user_id: ID of the user to get the RSS feed list for
        :return: List of RSS feeds of the user
        """
        if user_id not in self.tmp_feed_list.keys():
            return 1, {}
        return 0, {
            "user_id": user_id,
            "rss_feed_list":
                [rss_feed for rss_feed in self.tmp_feed_list[user_id]]
        }

    def add_rss_feed(self, user_id: int, rss_feed: str):
        """
        Adds a RSS feed to the list of users' RSS feeds
        :param user_id: ID of the user to add the feed to
        :param rss_feed: URL of the RSS feed to add to the user
        :return: Error code
        """
        current_feeds = self.tmp_feed_list.get(user_id, [])
        err_code, new_id = self._get_next_rss_id(user_id)
        assert err_code == 0
        new_entry = {
            "feed_id": new_id,
            "feed_url": rss_feed
        }
        current_feeds.append(new_entry)
        self.tmp_feed_list[user_id] = current_feeds
        return 0, {}

    def rm_rss_feed(self, user_id: int, rss_feed_id: int):
        """
        Removes a RS feed from the list of users' RSS feeds.
        :param user_id: ID of the user to remove the feed from
        :param rss_feed_id: ID of the RSS feed to remove from the users' feed
        :return: Error code
        """
        if user_id not in self.tmp_feed_list.keys():
            return 1
        rss_feeds = self.get_rss_feed_list(user_id)[1]['rss_feed_list']
        ids = [rss_feed['feed_id'] for rss_feed in rss_feeds]
        if rss_feed_id not in ids:
            return 2
        rss_to_remove = [a for a in rss_feeds if a['feed_id'] == rss_feed_id]
        assert len(rss_to_remove) == 1
        rss_feeds.remove(rss_to_remove[0])
        self.tmp_feed_list[user_id] = rss_feeds
        return 0
