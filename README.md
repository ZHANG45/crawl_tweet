# crawl_tweet

This is a simple python code what is used to crawl tweet through twitter API.

## Usage
To use it, first you need to apply for the access for yourself from https://apps.twitter.com/app/. After applying, you will get your 'consumer_key', 'consumer_secret', 'access_token', and 'access_token_secret'. Please remember to replace the part 'xxx' with your own information.

    consumer_key = 'xxx'
    consumer_secret = 'xxx'
    access_token = 'xxx'
    access_token_secret = 'xxx'

Then you can try to run it.

## Functions
This code contains several functions to get information from twitter.

    home_tweet(user): # get tweets showing in homepage of user
    get_all_friends(user, number): #get all information of user's friends
    get_status(user, number): #same as get_all_friends
    get_tweet(user, number): #get published tweet by user( only published in 7 days)
    search_tweet(user, query, number): #search tweet replies to user in 7 days that contains words in query 
