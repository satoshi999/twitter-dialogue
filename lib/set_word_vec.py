import sqlite3
import re
import emoji
from embedding import avg_enbedding

def set_word_vec(sqlite_config):
  conn = sqlite3.connect(sqlite_config['file_name'])

  cur = conn.cursor()

  results = cur.execute('SELECT * FROM tweets')

  for result in results:
    sentence = result[1].replace('\n', '')
    sentence = re.sub(r'https?:\/\/.+[\s]', '', result[1], flags=re.MULTILINE)
    sentence = re.sub('^@.+[\s]', '', result[1])
    sentence = ''.join(c for c in sentence if c not in emoji.UNICODE_EMOJI)

    vec = avg_enbedding(sentence)

    cur = conn.cursor()

    cur.execute(f"UPDATE tweets SET vec_str = '{str(vec)}' WHERE tweet_id = {result[0]}")

  conn.commit()
  conn.close()