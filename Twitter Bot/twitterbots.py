import tweepy #Twitter library
import time

auth = tweepy.0AuthHandler(consumer_key, consumer_secret) # Authentication for twitter API to verify account 
auth.set_access_token(access_token, access_token_secret)  # Set the access token for auth,

api = tweepy.API(auth)
user = api.me() 
user.name
user.screen_name
user.followers_count

public_tweets = api.name.home_timeline() # Grab public tweets
for tweet in public_tweets:
    print(tweet.text)


# BOT THAT FOLLOWS ALL FOLLOWERS

api = tweepy.API(auth)
user = api.me()  

def limit_handler(cursor):
    try: 
        while True:
            yield cursor.next() # Get the number the cursor moves through each
    except tweepy.RateLimitError:
        time.sleep(1000)

for follower in limit_handler(tweepy.Cursor(api.followers).items()): # cursor allows us to  paginate through followers list
    if follower.name == 'person1':
        follower.follow() # Follow a specific user 
        break
    print(follower.name) 


# BOT THAT LIKE TWEETS BASED ON CERTAIN WORDS WITHIN TWEET


api = tweepy.API(auth)
user = api.me()  

def limit_handler(cursor):   
    try:
        while True:
            yield cursor.next()
    except tweepy.RateLimitError:
        time.sleep(1000)

search_string = 'python' # search tweets with 'python' in
numberOfTweets = 2 # search for 2 tweets with condition
for tweet in tweepy.Cursor(api.search, search_string).items(numberOfTweets):
    try:
        tweet.favorite() # Like the tweets
        print('Tweet Liked')
    except tweepy.TweepError as e:
        print(e.reason)
    except StopIteration:
        break