# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
# coding: utf-8
import tweepy
import json
import xlsxwriter
import re

#your personal twitter key 
consumer_key = 'xxx'
consumer_secret = 'xxx'
access_token = 'xxx'
access_token_secret = 'xxx'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

def process_or_store(tweet):  #the type of crawled data is dict
    a =  json.dumps(tweet) #translate dtic into str
    return json.loads(a) #return str to dict

#functions to get twitter information
def home_tweet(user): # get tweets showing in homepage of user
    tweet_list = []
    for tweet in api.home_timeline(id = user): 
        tweet_list.append(tweet.text)
    return tweet_list
  
def get_status(user, number): #same as get_all_friends
    status_list = []
    for status in tweepy.Cursor(api.home_timeline,id=user).items(number):   
        status_list.append(process_or_store(status._json))
    return status_list
        
def get_all_friends(user, number): #get all information of user's friends
    friends_list = []
    for friend in tweepy.Cursor(api.friends, id=user).items(number): 
        friends_list.append(process_or_store(friend._json))
    return friends_list

def get_tweet(user, number): #get published tweet by user( only published in 7 days)
    tweet_list = []
    for tweet in tweepy.Cursor(api.user_timeline, id=user, tweet_mode="extended").items(number):   
        tweet_list.append(process_or_store(tweet._json))
        #tweet['text'] is the content of this tweet
        #tweet['user'] is the author of this tweet
        #tweet['entities']['hashtags'] is the tag contained in this tweet
        #tweet['retweet_count'] #is the times of this tweet being reteeted  
        #tweet['favorite_count'] #is the times of this tweet being liked
        #tweet['retweeted_status']['retweet_count']
        #tweet['retweeted_status']['favorite_count']
        #tweet['in_reply_to_status_id_str']   
    return tweet_list

def search_tweet(user, query, number): #search tweet replies to user in 7 days that contains words in query 
    tweet_list = []
    for tweet in tweepy.Cursor(api.search,q='to:'+user+ query).items(number): 
        tweet_list.append(process_or_store(tweet._json))
    return tweet_list

#write twitter information into excel file
def write_tweet_to_excel(user, number):
    #create excel file
    file_name = 'twitter-url-'+user+'.xlsx'
    wb = xlsxwriter.Workbook(file_name)
    ws = wb.add_worksheet()

    #set information of first row
    ws.write(0, 0, 'No.')
    ws.write(0, 1, 'twitter-id')
    ws.write(0, 2, 'twitter-text')

    i = 0 
    tweet_list = get_tweet(user,number)
    stop_list = [] # ['http', '@'] #if the tweet contains word in stop_list, then the tweet won't be put into excel
    
    for tweet in tweet_list:
        Flag = 0
        for stopword in stop_list:
            if stopword in stop_list:
                Flag = 1
                break
        if Flag != 1:
            ws.write(i+1, 0, i+1)
            ws.write(i+1, 1, str(tweet['id']))
            text = re.sub(r"http\S+", "", tweet['full_text']) #delete part of this tweet
            ws.write(i+1, 2, str(tweet['full_text']))       
            i = i + 1
    wb.close()#save file
    print(file_name, 'has been saved')

query = ' Ha OR haha OR hahaha OR lol'
user = "texashumor" #if user = '', then it will return your information
print(search_tweet(user, query, number=1)) #number limits how many tweets will be crawled
write_tweet_to_excel(user, number=20)
    
