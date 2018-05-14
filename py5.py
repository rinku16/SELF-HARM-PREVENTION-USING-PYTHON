import tweepy
from textblob import TextBlob
import json
from textblob.classifiers import NaiveBayesClassifier
import data


consumer_key = 'Kxb8kZktlNySFaotznj9OKT5W'
consumer_secret = '8q9UKrIhQJhM3QMf5ClJcKNVLceKlE9esJI2GLU0ROUUPwrI6M'

access_token = '975732708382068736-5xI0TIuGERrUzi4877ffOCJDek9C5us'
access_token_secret = 'SXRsrERcPAmMdgDgwEqpM8voXKvwHJvBLxoq6mxWqEtoA'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)


cl = NaiveBayesClassifier(data.train)

# Get the User object for twitter...
user = api.get_user('rinkuccet')

print ("NAME : "+user.screen_name)
print ("FOLLOWERS : "+ str(user.followers_count))

print("Friend's List  :")
for friend in user.friends():
   print (friend.screen_name)


public_tweets = api.home_timeline()

user_tweet = api.user_timeline()
i=1
print("\n#######################...........@"+user.screen_name + " user_timeline_tweet..........################\n")

#FOR PRINTING THE TWEET OF THE USER TO THE CONSOLE
for tweet in user_tweet:
	print("\nTweet "+str(i)+" : ")
	print("\nprediction :"+cl.classify(tweet.text))
	if cl.classify(tweet.text) == 'pos':

		print('Chance of self Harm is Low')	
	else:		
		print(tweet.text + "\nChance of self Harm is High")
	    
	
	analysis = TextBlob(tweet.text)
	print(analysis.sentiment)
	i = i + 1
	

print("\n#######################...........@"+user.screen_name + " Home_timeline_tweet..........################\n")

# FOR PRINTING THE tweetS TO THE CONSOLE
for tweet in public_tweets:
	print("\nTweet "+str(i)+" : ")
	print("\nPrediction :"+cl.classify(tweet.text))
	if cl.classify(tweet.text) == 'pos':
		print('Chance of self Harm is Low')	
	else:
		print(tweet.text + "\nChance of self Harm is High")
	analysis = TextBlob(tweet.text)
	print(analysis.sentiment)
	i = i + 1





# print(user.friends())
# for friend in user.friends():
#    print (friend.screen_name)



# prediction = cl.classify("all things are waste!!!")

# print("\nPrediction: "+prediction)

print("\nAccuracy training : " + str(cl.accuracy(data.train)))
print("\nAccuracy testing: " + str(cl.accuracy(data.test)))




