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


class RSSFeed:
    def __init__(self, rss_id: int, rss_url: str):
        self.rss_id = rss_id
        self.rss_url = rss_url


class NewsFetcher:
    def __init__(self):
        self.tmp_feed_list = dict()

    def _get_news_single_rss(self, rss_feed: str):
        pass

    def _get_next_rss_id(self, user_id: int):
        if user_id not in self.tmp_feed_list.keys():
            return 0, 0
        rss_feeds = self.get_rss_feed_list(user_id)
        ids = [rss_feed['feed_id'] for rss_feed in rss_feeds[1]['rss_feed_list']]
        return 0, max(ids) + 1

    def get_news_all_rss(self, user_id: int):
        pass

    def get_rss_feed_list(self, user_id: int):
        if user_id not in self.tmp_feed_list.keys():
            return 1, {}
        return 0, {
            "user_id": user_id,
            "rss_feed_list":
                [rss_feed for rss_feed in self.tmp_feed_list[user_id]]
        }

    def add_rss_feed(self, user_id: int, rss_feed: str):
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
