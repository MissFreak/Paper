# 只留下二、三、四字词
import pandas as pd
import numpy as np
df = pd.read_csv('chineselexicaldatabase2.1.csv')
df = df[df['Length'] != 1]
df = df[["Word", "Pinyin", 'C1Pinyin', 'C2Pinyin', 'C3Pinyin', 'Length',  'Frequency']]
df.sort_values(by=['Pinyin', 'Length','Frequency'], ascending=[True, True, False], inplace=True)
df.index = range(1, len(df) + 1)

# 得到df1是重复的-first
mask = df.duplicated(['C1Pinyin'])
df1 = df[mask]

# 得到df2是重复的
mask2 = df.duplicated(['C1Pinyin'],keep = False)
df2 = df[mask2]

#相减，得到first
target = pd.concat([df1, df2]).drop_duplicates(keep = False)

# 计算target的个数
target.shape[0]
# 将target保存起来
target.to_csv ('real-target.csv', header=True)

# 得到competitors
competitor = df2.loc[df2['C1Pinyin'].isin(target['C1Pinyin'])]
competitor.to_csv ('real-competitor.csv', header=True)

# 计算competitor的个数
competitor.shape[0] - target.shape[0]
--------------------------------------------------------------
df = pd.read_csv('chineselexicaldatabase2.1.csv')
df = df[df['Length'] > 2]
df = df[["Word", "Pinyin", 'C1Pinyin', 'C2Pinyin', 'C3Pinyin', 'Length',  'Frequency']]
df.sort_values(by=['Pinyin', 'Length','Frequency'], ascending=[True, True, False], inplace=True)
df.index = range(1, len(df) + 1)

df["2Pinyin"] = df["C1Pinyin"] + df["C2Pinyin"]

# 得到df1是重复的-first
mask = df.duplicated(['2Pinyin'])
df1 = df[mask]

# 得到df2是重复的
mask2 = df.duplicated(['2Pinyin'],keep = False)
df2 = df[mask2]

#相减，得到first
target = pd.concat([df1, df2]).drop_duplicates(keep = False)

# 计算target的个数
target.shape[0]
# 将target保存起来
target.to_csv ('real-target.csv', header=True)

# 得到competitors
competitor = df2.loc[df2['2Pinyin'].isin(target['2Pinyin'])]
competitor.to_csv ('real-competitor.csv', header=True)

# 计算competitor的个数
competitor.shape[0] - target.shape[0]
------------------------------------------------------------------
df = pd.read_csv('chineselexicaldatabase2.1.csv')
df = df[df['Length'] > 3]
df = df[["Word", "Pinyin", 'C1Pinyin', 'C2Pinyin', 'C3Pinyin', 'Length',  'Frequency']]
df.sort_values(by=['Pinyin', 'Length','Frequency'], ascending=[True, True, False], inplace=True)
df.index = range(1, len(df) + 1)

df["3Pinyin"] = df["C1Pinyin"] + df["C2Pinyin"] + df["C3Pinyin"]

# 得到df1是重复的-first
mask = df.duplicated(['3Pinyin'])
df1 = df[mask]

# 得到df2是重复的
mask2 = df.duplicated(['3Pinyin'],keep = False)
df2 = df[mask2]

#相减，得到first
target = pd.concat([df1, df2]).drop_duplicates(keep = False)

# 计算target的个数
target.shape[0]
# 将target保存起来
target.to_csv ('real-target3.csv', header=True)

# 得到competitors
competitor = df2.loc[df2['3Pinyin'].isin(target['3Pinyin'])]
competitor.to_csv ('real-competitor3.csv', header=True)

# 计算competitor的个数
competitor.shape[0] - target.shape[0]
