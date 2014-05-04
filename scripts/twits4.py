#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Devin
#
# Created:     30/03/2014
# Copyright:   (c) Devin 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------


import tweepy
import csv

'''
#for logging events
import logging
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
'''
# Consumer keys and access tokens, used for OAuth
consumer_key = '6DKDpKaqvhg2n6GBDrrHw'
consumer_secret = 'SYdPMUwCU0gFfG9qXWAxYGqHR9SggDASmavSvWnrYE'
access_token = '457804868-XBLeyFfxoYSYaP9UT7FCOBhldFgsojs9DVkPUnuH'
access_token_secret = 'O6B8Q8F3DBmsUxFf4i7p5KSPJsxydz4MFCkJYpyGRevwM'

# OAuth process, using the keys and tokens
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

# Creation of the actual interface, using authentication
api = tweepy.API(auth)

# Creates the user object. The me() method returns the user whose authentication keys were used.
user = api.me()

#pulls all tweets form the last 5 days into an array
tweets = []
'''
with open('twits.csv', 'wb') as csvfile:
	while True:
		for tweet in tweepy.Cursor(api.search,
								   q="%40tide",
								   rpp=10,
								   result_type="recent",
								   include_entities=True,
								   lang="en").items():
			#print tweet.created_at, tweet.text.encode('utf-8')

			twitwriter = csv.writer(csvfile, delimiter = '')
			twitwriter.writerow(tweet.text.encode('utf-8') + '|')
		else:
			break
		#tweets.append(tweet.text.encode('utf-8'))
		#print tweet.created_at, tweet.text.encode('utf-8')
'''
keyword="%40tide"
#result = tweepy.api.search(q=keyword,rpp=1000,page=2)

result = tweepy.Cursor(api.search,
   q="%40tide",
   rpp=10,
   result_type="recent",
   include_entities=True,
   lang="en").items()

with open('twits2.csv', 'wb') as acsv:
    w = csv.writer(acsv)
    #w.writerow(('Tweet'))
    for tweet in result:
        w.writerow([tweet.text.encode('utf-8')])




	
#prints first tweet in list
#print tweets[1]
'''
with open('twits.csv', 'wb') as csvfile:
	twitwriter = csv.writer(csvfile)
	for tweet in tweets:
		twitwriter.writerow(tweet)
'''	
	

'''
lda = LdaModel(tweets, num_topics = 10)
doc_lda = lda[doc_bow]
print(lda[doc_bow])
'''
