# -*- coding: utf-8 -*-

import numpy as np
import pandas as pd
from pathlib import Path
import matplotlib.pyplot as plt

DATA_DIR = Path('./data/')

answer = ['10分未満', '10分～30分', '30分～1時間', '1時間以上']#化粧全般の選択肢
answer_b = ['5分未満', '5分～10分', '10分～15分', '15分～30分', '30分以上']#ベースメイクの選択肢

df1 = pd.read_csv(DATA_DIR /'q5.csv')
df2 = pd.read_csv(DATA_DIR /'q7.csv')
#df1 = pd.read_csv(DATA_DIR /'q6.csv')
#df2 = pd.read_csv(DATA_DIR /'q8.csv')

output = pd.DataFrame(columns = []) 


for index, row in df1.iterrows():

    i = answer.index(row['ans_5'])
#    i = answer_b.index(row['ans_6'])
    df_id = row['id']
    print(df_id)

    for i in range(3):
        df= df2[(df2['id']==df_id) & (df2['ans_7']==answer[i+1])]
#        df= df2[(df2['id']==df_id) & (df2['ans_8']==answer_b[i+1])]
        output = output.append(df, ignore_index = True)

output.to_csv(DATA_DIR / 'q57.csv', index=None)
#output.to_csv(DATA_DIR / 'q68.csv', index=None)