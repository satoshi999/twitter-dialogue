import os
import sqlite3

def db_init(sqlite_config):
    if os.path.isfile(sqlite_config['file_name']) == True:
        os.remove(sqlite_config['file_name']) 

    conn = sqlite3.connect(sqlite_config['file_name'])

    cur = conn.cursor()

    cur.execute(
        'CREATE TABLE IF NOT EXISTS reply_tweet ( \
            tweet_id INTEGER PRIMARY KEY, \
            tweet_text TEXT, \
            vec_str TEXT, \
            vec INTEGER, \
            user_id INTEGER, \
            screen_name TEXT, \
            in_reply_to_screen_name TEXT, \
            in_reply_to_status_id INTEGER )')

    cur.execute(
        'CREATE TABLE IF NOT EXISTS tweets( \
            tweet_id INTEGER PRIMARY KEY, \
            tweet_text TEXT, \
            vec_str TEXT, \
            vec INTEGER, \
            user_id INTEGER, \
            screen_name TEXT)')

    cur.execute(
        'CREATE TABLE IF NOT EXISTS trends( \
            name TEXT PRIMARY KEY)')

    cur.execute(
        'CREATE TABLE IF NOT EXISTS trend_tweet_users( \
            user_id INTEGER PRIMARY KEY, \
            screen_name TEXT)')

    conn.commit()
    conn.close()