#筛选出含有二声和三声的词语
import pandas as pd
import numpy as np
df = pd.read_csv('chineselexicaldatabase2.1.csv')
filter = df['Pinyin'].str.contains('2|3',regex=True)
df = df[filter]
newdf = df[["Word", "Pinyin", 'Length', 'Frequency']]
newdf['Pinyin'].replace('\d', '', regex=True, inplace = True)
newdf['Pinyin2'] = df['Pinyin']
newdf = newdf[["Word", "Pinyin",'Pinyin2', 'Length', 'Frequency']]


#按照拼音、长度和频率排序，得到一个含有32445个词语的语料库，保存成新文件
newdf.sort_values(by=['Pinyin', 'Length','Frequency'], ascending=[True, True,False], inplace=True)
newdf.index = range(1, len(newdf) + 1)
newdf['C2Tone'] = newdf['C2Tone'].astype(int, copy=False, errors='ignore')
newdf['C4Tone'] = newdf['C4Tone'].astype(int, copy=False, errors='ignore')
#newdf.to_csv ('newList.csv', header=True)

# #筛选出pseudo-homophones，保存成一个新的dataframe
# 先去掉音节不重复的词语，因为音节必须相同
mask = newdf.duplicated(['Pinyin'],keep = False)
newdf_1 = newdf[mask]
# 计算real homophony的个数: 9751
newdf_1.shape[0]

# 然后把二声都变成三声
newdf_1['Pinyin3'] = newdf_1['Pinyin2'].replace('2', '3', regex=True)

# 取出变化的rows
newdf_2 = newdf_1.loc[newdf_1['Pinyin2'] != newdf_1['Pinyin3']]

# 取出没有变化的rows
newdf_3 = newdf_1.loc[newdf_1['Pinyin2'] == newdf_1['Pinyin3']]

#将变化的rows匹配没有变化的rows
# Dict = {}
List = []
List_2 = []
for index, row in newdf_2.iterrows():
    for i in range(-20, 20):
        if (index+i) in range(1, len(newdf) + 1):
            try:
                if row['Pinyin3'] == newdf_3.get_value(index+i, 'Pinyin3'):
                    # Dict.update({index+i: index})
                    List.append(index)
                    List_2.append(index+i)
            except: continue

# 计算pseudo的个数：(index的个数)
len(List)


# #将字典放进一个不重复的列表
# list = []
# for key, value in Dict.items():
#     if key not in list:
#         list.append(key)
#     if value not in list:
#         list.append(value)

#取出列表的rows，形成新的dataframe
newdf_4 = newdf_1[newdf_1.index.isin(List)]
newdf_5 = newdf_1[newdf_1.index.isin(List_2)]
newdf_4['Length'].value_counts()

# #给新的dataframe排序，保存到文件中
# newdf_4.sort_values(by=['Length', 'Pinyin', 'Frequency'], ascending=[True, True, False], inplace=True)
# newdf_4.index = range(1, len(newdf_4) + 1)
#newdf_4.to_csv ('newList_5.csv', header=True)
