import os
from os.path import join, dirname
from dotenv import load_dotenv
from requests_oauthlib import OAuth1Session

# envファイルを読み込み
dotenv_path = join(dirname(__file__), 'env/.env')
load_dotenv(dotenv_path)

# twitter apiキーをセット
twiApi = OAuth1Session(os.environ.get('TWI_CONSUMER_KEY'),
                    os.environ.get('TWI_CONSUMER_SECRET'),
                    os.environ.get('TWI_TOKEN'),
                    os.environ.get('TWI_TOKEN_SECRET'))

# docomo対話 apiキーをセット
docomoApi = os.environ.get('DOCOMO_API')

replAiApiKey = os.environ.get('REPLAI_API_KEY')
replAiApiBotid = os.environ.get('REPLAI_API_BOTID')
