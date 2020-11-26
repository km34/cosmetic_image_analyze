# -*- coding: utf-8 -*-

import pandas as pd 
from pathlib import Path

DATA_DIR = Path('./data/')

df = pd.read_csv(DATA_DIR / 'q10.csv' )
df2 = pd.read_csv(DATA_DIR / 'q15.csv')
output = pd.DataFrame(columns = [])
i= 0
#df= df[df['ans_10'].str.contains('自己流')]
#output =  output.append(df, ignore_index = True)
for index, row in df.iterrows():
    if row['ans_10'].find('自己流'):
        i = i+1 #なんか数少ない
        df_id = row['id']
        df_target = df2[(df2['id']==df_id) & (df2['ans_15'].str.contains('ムラ') | df2['ans_15'].str.contains('むら')| df2['ans_15'].str.contains('厚') | df2['ans_15'].str.contains('塗り') ) ]
        output =  output.append(df_target, ignore_index = True)

output.to_csv(DATA_DIR / 'q1015.csv', index=None)
print(i)