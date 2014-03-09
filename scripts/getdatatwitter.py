import requests
from rauth import OAuth1Service
from rauth import OAuth1Session

consumer_key = ''' enter key '''
consumer_secret = ''' enter key '''
access_token = ''' enter key '''
access_token_secret = ''' enter key '''

oauth_service = OAuth1Service(consumer_key = consumer_key, 
                            consumer_secret = consumer_secret)
oauth_session = oauth_service.get_session(token = (access_token, access_token_secret))

twitter_handle = #enter twitter handle
url = 'https://api.twitter.com/1.1/search/tweets.json?q=%40' + twitter_handle
# params = ''include_rts': 'true''
r = oauth_session.get(url, params={}) # THIS WORKS