from twitter import *
import sqlite3

def trend_tweet_users(sqlite_config, twitter_config):
    t = Twitter(auth=OAuth(
        twitter_config['access_token'], 
        twitter_config['access_token_secret'], 
        twitter_config['consumer_key'], 
        twitter_config['consumer_secret_key']
        ))

    conn = sqlite3.connect(sqlite_config['file_name'])

    cur = conn.cursor()

    results = cur.execute("SELECT * from trends")

    users = {}

    for result in results:
        tweets = t.search.tweets(q=result[0])

        for tweet in tweets['statuses']:
            users[str(tweet['user']['id'])] = tweet['user']['screen_name']

    for key in users:
        user_id = key
        screen_name = users[key]
        cur.execute("INSERT INTO trend_tweet_users values('" + user_id + "', '" + screen_name + "')")

    conn.commit()
    conn.close()
