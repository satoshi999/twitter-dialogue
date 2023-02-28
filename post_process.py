import yaml
from lib.init import db_init
from lib.trends import trends
from lib.trend_tweet_users import trend_tweet_users
from lib.tweet import to_tweet, replyed_tweet
from lib.enbedding import set_word_vec

sqlite_config = {}
twitter_config = {}

print('--- load config ---')
with open('./config/config.yaml') as file:
    config = yaml.safe_load(file.read())
    sqlite_config = config['sqlite3']
    twitter_config = config['twitter']

print('--- init ---')
db_init(sqlite_config)
print('--- get trends ---')
trends(sqlite_config, twitter_config)
print('--- get trend tweet users')
trend_tweet_users(sqlite_config, twitter_config)
print('--- get to tweet')
to_tweet(sqlite_config, twitter_config)
print('--- get replyed tweet ---')
replyed_tweet(sqlite_config, twitter_config)
print('--- set word vec ---')
set_word_vec(sqlite_config)