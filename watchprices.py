import praw
import sched, time
import os

from twilio.rest import Client

# Reddit API credentials
client_id = os.environ.get('REDDIT_CLIENT_ID')
client_secret = os.environ.get('REDDIT_CLIENT_SECRET')
user_agent = os.environ.get('REDDIT_USER_AGENT')

# Your Twilio Account SID and Auth Token
account_sid = os.environ.get('TWILIO_ACCOUNT_SID')
auth_token = os.environ.get('TWILIO_AUTH_TOKEN')

# Create a Twilio client
client = Client(account_sid, auth_token)

# Authenticate with Reddit API
reddit = praw.Reddit(
    client_id=client_id,
    client_secret=client_secret,
    user_agent=user_agent
)

priceList = {}

# Fill with what you want
brands_to_check = ['longines', 'Tudor']

print('-----Launching-----')

# Subreddit to monitor
subreddit_name = 'WatchExchange'

# Fetch new posts from the subreddit
subreddit = reddit.subreddit(subreddit_name)

def getWatchPrices(scheduler):
    # schedule the next call first
    scheduler.enter(30, 1, getWatchPrices, (scheduler,))
    print("Doing stuff...")
    # then do your stuff

    new_posts = subreddit.new(limit=10)

    print('~Getting New Prices~')

    # Filter and process the posts
    for post in new_posts:

        # Create hash from post data
        hashValue = hash(f"{post.created_utc}{post.title}")

        if hashValue in priceList:
            # We have the data already, do nothing
            print("Already Stored Data")
        else: 
            # We don't have the data, need to add
            # Check if dictionary is full
            priceList[hashValue] = f"{post.created_utc},{post.link_flair_text},{post.title},{post.url}"

            print(f"STORING: {post.link_flair_text} - {post.title} - CREATED ON {post.created_utc}")

            # Check for keywords
            for keyword in brands_to_check:
                if keyword in post.title:
                    # We are interested to send
                    # Sending a text message
                    message = client.messages.create(
                        body="⌚" + f"{post.link_flair_text} : {post.title} : {post.url}",
                        from_=os.environ.get('TWILIO_NUM'),  # Your Twilio phone number
                        to=os.environ.get('TWILIO_REP_NUM')  # Recipient's phone number
                    )

    if len(priceList) > 30:
        # List too large, clean oldest entries
        for x in range(0,9):
            print("Clearing data...")
            priceList.pop(next(iter(priceList)))
    else:
        print("Dictionary Length " + str(len(priceList)))

my_scheduler = sched.scheduler(time.time, time.sleep)
my_scheduler.enter(30, 1, getWatchPrices, (my_scheduler,))
my_scheduler.run()