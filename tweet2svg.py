#! /usr/bin/env python

import time, sys, os
from shutil import rmtree

import tweepy

from streamListener import SListener
from oAuth import *

# OAuth process, using the keys and tokens
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

def main():
	hashtags = []
	if len(sys.argv) >= 2:
		for hashtag in sys.argv[1:]:
			hashtags.append("#" + hashtag)

	users=[]
		 
	listen = SListener(api, 'test')
	stream = tweepy.Stream(auth, listen)

	print "Streaming started on %s keywords and %s users...\n" % (len(hashtags), len(users))
	
	if os.path.exists("images"):
		rmtree("images")
	os.makedirs("images")

	try: 
		if not hashtags and not users:
			stream.sample()
		else:
			stream.filter(track = hashtags, follow = users)
	except (KeyboardInterrupt, SystemExit):
		print "\nProgram Terminated."
		stream.disconnect()
	except:
		stream.disconnect()
		raise


if __name__ == '__main__':
	main()


	





