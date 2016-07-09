import json
import time
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import os

consumer_key = 'rbL3r0ooU9eWPdV8gmyXzk8UG'
consumer_secret = 'W6ZpcOLJATyptjjIcjfeqK2p87rSMdD5tFDttYDMVWrxvGf3bY'
access_token = '4315260679-4yy5RLUBAaMYjU1TyFhPft7gAvVZT2DY2W05uRN'
access_token_secret = 'xu8QMrnOpRktQrhTfus50VGyPdJt3BTOjgNwx9BW4jSqD'

class StdOutListener(StreamListener):
	def on_data(self,data):
		try:
			savefile = open("C:\Users\Anand\Desktop\output2.json",'a')
			savefile.write(data)
			# savefile.write(",")
			# savefile.close()
			return True
		except BaseException,e:
			print "failed",str(e)
			time.sleep(5)

	def on_error(self,status):
		print(status)
	
	def on_timeout(self):
		print('Timeout')
		return True

if __name__=='__main__':
	listener= StdOutListener()
	auth = OAuthHandler(consumer_key, consumer_secret)
	auth.set_access_token(access_token, access_token_secret)
	stream=Stream(auth,listener)
	stream.filter(track=['python'])