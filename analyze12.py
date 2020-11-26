# -*- coding: utf-8 -*-

import numpy as np 
import pandas as pd 
import MeCab
from pathlib import Path 
import collections

DATA_DIR = Path('./data/')

#無回答を削除し，回答を結合する
""" df = pd.DataFrame(columns = [])
target = pd.read_csv(DATA_DIR / f'q14.csv')
target = target[(target['ans_14'] != '購入するときに苦労はない') ]
target = target[ (target['ans_14'] != '購入する時に苦労はない')]
target = target[(target['ans_14'] != '苦労はない') ]
target = target[(target['ans_14'] != '特にない') ]
df = df.append(target, ignore_index = True)
df.to_csv(DATA_DIR / 'q145.csv', index=None)

list_df = df['ans_14'].values.tolist()
sentence = ''.join(list_df)
 """

""" df = pd.DataFrame(columns = [])
target = pd.read_csv(DATA_DIR / f'q15.csv')
target = target[(target['ans_15'] != '塗るときに苦労はない') ]
target = target[ (target['ans_15'] != '塗る時に苦労はない')]
target = target[(target['ans_15'] != '苦労はない') ]
target = target[(target['ans_15'] != '特にない') ]
df = df.append(target, ignore_index = True)
df.to_csv(DATA_DIR / 'q155.csv', index=None)

list_df = df['ans_15'].values.tolist()
sentence = ''.join(list_df)
 """


df = pd.DataFrame(columns = [])
target = pd.read_csv(DATA_DIR / f'q16.csv')
target = target[(target['ans_16'] != '特にない') ]
target = target[(target['ans_16'] != '特になし') ]
df = df.append(target, ignore_index = True)
df.to_csv(DATA_DIR / 'q165.csv', index=None)

list_df = df['ans_16'].values.tolist()
sentence = ''.join(list_df)

#print(sentence)


#頻出単語を探し，その意見数を数えたい


m = MeCab.Tagger ('-Ochasen')
 
node = m.parseToNode(sentence)
words=[]
while node:
    hinshi = node.feature.split(",")[0]
    if hinshi in ["名詞","動詞","形容詞"]:
        origin = node.feature.split(",")[6]
        words.append(origin)
    node = node.next

c = collections.Counter(words)
print(c.most_common(20))