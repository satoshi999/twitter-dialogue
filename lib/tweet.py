from twitter import *
import sqlite3

def to_tweet(sqlite_config, twitter_config):
    t = Twitter(auth=OAuth(
        twitter_config['access_token'], 
        twitter_config['access_token_secret'], 
        twitter_config['consumer_key'], 
        twitter_config['consumer_secret_key']
        ))

    conn = sqlite3.connect(sqlite_config['file_name'])

    cur = conn.cursor()

    results = cur.execute('SELECT * FROM trend_tweet_users')

    for result in results:

        try:
            tweets = t.search.tweets(q="to:" + result[1], lang='ja')

            for tweet in tweets["statuses"]:
                
                sql = f"INSERT INTO reply_tweet( \
                    tweet_id,  \
                    tweet_text,  \
                    user_id,  \
                    screen_name,  \
                    in_reply_to_screen_name,  \
                    in_reply_to_status_id)  \
                    values ( \
                    {tweet['id']} , \
                    '{tweet['text']}' , \
                    {tweet['user']['id']} , \
                    '{tweet['user']['screen_name']}' , \
                    '{tweet['in_reply_to_screen_name']}' , \
                    {tweet['in_reply_to_status_id']})"

                cur = conn.cursor()
                cur.execute(sql)
        except Exception as e:
            print(e)
            continue

    conn.commit()
    conn.close()

def replyed_tweet(sqlite_config, twitter_config):
    t = Twitter(auth=OAuth(
        twitter_config['access_token'], 
        twitter_config['access_token_secret'], 
        twitter_config['consumer_key'], 
        twitter_config['consumer_secret_key']
        ))

    conn = sqlite3.connect(sqlite_config['file_name'])

    cur = conn.cursor()

    results = cur.execute('SELECT * FROM reply_tweet')

    for result in results:
        try:
            tweet = t.statuses.show(id=result[7])

            cur = conn.cursor()
            
            sql = f"INSERT INTO tweets( \
                    tweet_id,  \
                    tweet_text,  \
                    user_id,  \
                    screen_name  \
                    ) values (  \
                    {tweet['id']},  \
                    '{tweet['text']}',  \
                    {tweet['user']['id']},  \
                    '{tweet['user']['screen_name']}'  \
                    )"

            cur.execute(sql)
        except Exception as e:
            print(e)
            continue


    conn.commit()
    conn.close() 
