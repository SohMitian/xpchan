import apiKey
import json

class twicon:  # Twitter上の操作クラス
    # コンストラクタ
    def __init__(self):
        # apiKey設定
        api = apiKey.twiApi
        
        # urlList [0:検索ツイート取得, 1:タイムライン取得 2:ツイートする, 3:RTする](取得:GET, する:POST)
        URL_LIST = ['https://api.twitter.com/1.1/search/tweets.json',
                    'https://api.twitter.com/1.1/statuses/home_timeline.json',
                    'https://api.twitter.com/1.1/statuses/update.json',
                    'https://api.twitter.com/1.1/statuses/retweet/:id.json']

        # 検索ワード(RTは含まない)
        SERCH_WORD = ['#XPちゃん -rt',
                      '#XPchan -rt',
                      'XPちゃん -rt',
                      'XPchan -rt']

        self.twitter = api
        self.url = URL_LIST
        self.word = SERCH_WORD

    # 検索
    def serch(self):
        params = {'q': self.word, 'count': 100}
        serch = self.twitter.get(self.url[0], params=params)
        if serch.status_code == 200:
            # 検索データをディクショナリで返す
            #print('ok') # デバッグ用
            return json.loads(serch.text)
            
        else:
            return 404

    # RT
    def rt(self, serch):
        if serch != 404:
            search_tweet = serch
            for tweet in search_tweet['statuses']:
                # NGワード(check:ワードの増加を想定し、別ファイルを用意)
                if not '@tip_XPchan' in tweet['text'] or 'bot' in tweet['user']['screen_name']:
                    #print('ok') # デバッグ用
                    #if tweet['retweet_count'] > 2 and tweet['favorite_count'] > 2:
                    url = self.url[3].replace(':id', str(tweet['id']))
                    self.twitter.post(url)
        else:
            return 404

    # tweet
    def tweet(self, text):
        if text != 404:
            print('hoge')
