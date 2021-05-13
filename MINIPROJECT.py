"""      MINIPROJECT BY PRAPTI RANA
           STUDENT OF SEMESTER 4
              2014772
            B.TECH CSE (CORE)
            """
import tweepy
import matplotlib.pyplot as plt
from textblob import TextBlob

#all authentication keys to access twitter API
# to connect as or to jump to server/ reverse the proxy server
consumer_key = "8AO6OU5ubyi4XO47b1C7Sjdlz"
consumer_sec = "FS1usPrfPolvjLXbwGka5N8TWkOZhUsdxGmmTwuO016koesUSt"
# from proxy server in order to connect to server
access_token = "1151573806680592384-OUFeUtpsRFZM6jQxl1AG99NEjlY0Kt"
access_token_sec = "KKHmkHkDGVaDof8XK4fKKI52DmNl4vZlaXnx85WRfd4Lr"
# tweepy exploration
dir(tweepy)

# to connect to jump server of twitter
auth=tweepy.OAuthHandler(consumer_key,consumer_sec)

# now we need to connect from jump server to web server of twitter
auth.set_access_token(access_token,access_token_sec)

#now we can connect to the API storage server on twitter
api_connect=tweepy.API(auth)

#now we can search any topic on twitter
tweet_data=api_connect.search('India',count=100)

pos=0   #positive tweets
neg=0   #negative tweets
neu=0   #neutral tweets

#printing in line by line
for tweet in tweet_data:
    #print(tweet.text)
    analysis=TextBlob(tweet.txt)    #here it will apply NLP\
    print(analysis.sentiment)
    #now checking polarity only
    if analysis.sentiment.polarity >0:
    print("POSITIVE")
    pos=pos+1
    elif analysis.sentiment.polarity ==0:
        print("NEUTRAL")
        neu=neu+1
        else :
            print("NEGATIVE")
            neg=neg+1


# TO PLOTING THE GRAPH
plt.xlabel("tags")
plt.ylabel("polarity")
#plt.bar(['pos','neg','neu'],[pos,neg,neu])
plt.pie[pos,neg,neu],labels=['pos','neg','neu'],autopct="%1.1f%%"
plt.show()
