from twitter import *
import sqlite3

def trends(sqlite_config, twitter_config):
    t = Twitter(auth=OAuth(
        twitter_config['access_token'], 
        twitter_config['access_token_secret'], 
        twitter_config['consumer_key'], 
        twitter_config['consumer_secret_key']
        ))

    conn = sqlite3.connect(sqlite_config['file_name'])

    cur = conn.cursor()

    trends = t.trends.place(_id=1)

    for trend in trends[0]['trends']:
        cur.execute("INSERT INTO trends values ('" + trend['name'] + "')")

    conn.commit()
    conn.close()
