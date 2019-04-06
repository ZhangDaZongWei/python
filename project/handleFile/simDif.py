# 利用编辑距离算法，计算相似度

from similarity.normalized_levenshtein import NormalizedLevenshtein

def simDif(w1,w2):
  normalized_levenshtein = NormalizedLevenshtein()
  dis = normalized_levenshtein.distance(w1,w2)
  sim = normalized_levenshtein.similarity(w1,w2)
  print('distance: '+str(dis)+' similarity: '+ str(sim))
  # 此线表示的是固定文本的一段和活动文本各段比较之后的分隔
  print('----------------------------')
  # return sim
