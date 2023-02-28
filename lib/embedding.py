import MeCab
import gensim
import numpy as np
import logging
from sklearn.metrics.pairwise import cosine_similarity

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

print('--- load word2vec model ---')
model = gensim.models.KeyedVectors.load_word2vec_format('cc.ja.300.vec.gz', binary=False)
model.fill_norms()
wakati = MeCab.Tagger("-Owakati")

def cos_similarity(v1, v2):
  v1 = np.array(v1)
  v2 = np.array(v2)
  #print(cosine_similarity(np.array([v1]) , np.array([v2])))
  #print(np.dot(v1, v2) / (np.linalg.norm(v1) * np.linalg.norm(v2)))

  return np.dot(v1, v2) / (np.linalg.norm(v1) * np.linalg.norm(v2))

def avg_enbedding(sentence):
  words = wakati.parse(sentence).split()

  sum_vec = np.zeros(300)
  count = 0
  for word in words:
    if word in model.key_to_index:
      sum_vec += model[word]
      count += 1

  if count <= 0:
    return sum_vec
  else:
    return sum_vec / count