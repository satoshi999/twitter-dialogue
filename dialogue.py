import sqlite3
import random
import json
from lib.embedding import avg_enbedding, cos_similarity
import yaml
import numpy as np
import logging
import re
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

conn = {}

max_answer = 5

with open('./config/config.yaml') as file:
    config = yaml.safe_load(file.read())
    conn = sqlite3.connect(config['sqlite3']['file_name'])


while True:

    cur = conn.cursor()
    results = cur.execute('SELECT j.* FROM tweets j, reply_tweet r where j.tweet_id = r.in_reply_to_status_id')

    val = input('----- >>>> ')
    if val == 'exit':
        break

    query = avg_enbedding(val)

    dic = {}
    for result in results:
        
        vec_str = result[2].replace('[', '').replace(']', '')
        vec = np.fromstring(vec_str, dtype=float, sep=' ')

        sim = cos_similarity(query, vec)
        
        dic[sim] = {'tweer_id': result[0], 'tweet_text': result[1], 'screen_name': result[5]}

    dict = sorted(dic.items(), reverse=True)

    #logger.debug(json.dumps(dict, indent=2, ensure_ascii=False))

    for i in range(max_answer):
        cur = conn.cursor()
        replys = cur.execute(f"SELECT * FROM reply_tweet WHERE in_reply_to_status_id = {dict[i][1]['tweer_id']}")
        r_list = replys.fetchall()
        for r in r_list:
            sentence = re.sub('^@.+[\s]', '', r[1])

            print('\n')
            print(sentence)
            print('\n')
        


conn.close()