import MeCab
import numpy as np
import sqlite3
import re
import emoji
import yaml

wakati = MeCab.Tagger("-Owakati")


def avg_enbedding(sentence):
  words = wakati.parse(sentence).split()

  sum_vec = np.zeros(300)
  count = 0
  for word in words:
      count += 1

  print(count)

def update_enbedding(sqlite_config):
  conn = sqlite3.connect(sqlite_config['file_name'])

  cur = conn.cursor()

  results = cur.execute('SELECT * FROM tweets')

  for result in results:
    sentence = result[1].replace('\n', '')
    sentence = re.sub(r'https?:\/\/.+[\s]', '', result[1], flags=re.MULTILINE)
    sentence = re.sub('^@.+[\s]', '', result[1])
    #sentence = ''.join(c for c in sentence if c not in emoji.UNICODE_EMOJI)

    vec = avg_enbedding(sentence)


  conn.close()

with open('./config/config.yaml') as file:
    config = yaml.safe_load(file.read())
    sqlite_config = config['sqlite3']
    twitter_config = config['twitter']

update_enbedding(sqlite_config)