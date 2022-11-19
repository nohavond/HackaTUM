import feedparser


class NewsFetcher:
    def __init__(self):
        self.tmp_feed_list = dict()

    def _get_news_single_rss(self, rss_feed: str):
        pass

    def get_news_all_rss(self, user_id: int):
        pass

    def get_rss_feed_list(self, user_id: int):
        pass

    def add_rss_feed(self, user_id: int, rss_feed: str):
        pass

    def rm_rss_feed(self, user_id: int, rss_feed_id: int):
        pass
