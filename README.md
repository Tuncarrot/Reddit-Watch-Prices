# Python Reddit Market Observer

The following python program calls the Reddit API to monitor a market related subreddit. 
In this case, we are monitoring R/WatchExchange with keywords and using Twilio to message results directly to your phone including a link, however you can monitor any subreddit.

In order to use this script correctly, you will need to register for both a [reddit API key](https://www.reddit.com/dev/api/) and a [Twilio](https://www.twilio.com/en-us) account

## API Credentials
When you have your keys, create environment variables for the following keys and assign them accordingly

**Reddit Related Keys**

REDDIT_CLIENT_ID

REDDIT_CLIENT_SECRET

REDDIT_USER_AGENT


**Twilio Related Keys**

TWILIO_ACCOUNT_SID

TWILIO_AUTH_TOKEN

Use the brands_to_check variable to input whatever you want to track.


![Capture](https://github.com/Tuncarrot/Reddit-Watch-Prices/assets/31707034/b1216a3e-3669-4cec-8986-2641bc74ac9a)

![IMG_2740](https://github.com/Tuncarrot/Reddit-Watch-Prices/assets/31707034/c842d4bf-fc74-4203-b292-1ecd0b466108)
