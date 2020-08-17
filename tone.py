#筛选出含有二声和三声的词语
import pandas as pd
import numpy as np
df = pd.read_csv('chineselexicaldatabase2.1.csv')
filter = df['Pinyin'].str.contains('2|3',regex=True)
df = df[filter]
newdf = df[["Word", "Pinyin", 'C1Pinyin', 'C1Tone', 'C2Pinyin', 'C2Tone', 'C3Pinyin', 'C3Tone', 'C4Pinyin', 'C4Tone', 'Length',  'Frequency']]
newdf['Pinyin'].replace('\d', '', regex=True, inplace = True)
newdf['Pinyin2'] = df['Pinyin']
newdf = newdf[["Word", "Pinyin",'Pinyin2', 'C1Pinyin', 'C1Tone', 'C2Pinyin', 'C2Tone', 'C3Pinyin', 'C3Tone', 'C4Pinyin', 'C4Tone', 'Length',  'Frequency']]


#按照拼音、长度和频率排序，得到一个含有32445个词语的语料库，保存成新文件
newdf.sort_values(by=['Pinyin', 'Length','Frequency'], ascending=[True, True,False], inplace=True)
newdf.index = range(1, len(newdf) + 1)
newdf.shape[0]
newdf['C2Tone'] = newdf['C2Tone'].astype(int, copy=False, errors='ignore')
newdf['C4Tone'] = newdf['C4Tone'].astype(int, copy=False, errors='ignore')
#newdf.to_csv ('newList.csv', header=True)

# #筛选出pseudo-homophones，保存成一个新的dataframe
# 先去掉音节不重复的词语，因为音节必须相同
mask = newdf.duplicated(['Pinyin'],keep = False)
newdf_1 = newdf[mask]
newdf_1['Pinyin3'] = newdf_1['Pinyin2'].replace('2', '3', regex=True)


# 然后找出所有的组合
dict = {k: tuple(d.index) for k, d in newdf_1.groupby('Pinyin') if len(d) > 1}
len(dict)



# 把所有2声换成3声，匹配其他词语
Dict = {}
for key, value in dict.items():
    if newdf_1.at[value[0], 'Pinyin2'].str.contains('2',regex=True):
        newdf_1.at[value[0], 'Pinyin2'].str.replace('2', '3')





# #先筛选出单音节词,共1579个；去掉不重复的单音节词，剩余1510个
# pseudohomo1 = newdf[newdf['Length'] == 1]
# mask = pseudohomo1.duplicated(['Pinyin'],keep = False)
# pseudohomo1 = pseudohomo1[mask]
# pseudohomo1.shape[0]

# #再筛选出双音节词，共22364个，去掉不重复的单音节词，剩余8106个；去掉完全相同的单音节词，剩余5496个；
# pseudohomo2 = newdf[newdf['Length'] == 2]
# mask = pseudohomo2.duplicated(['Pinyin'],keep = False)
# pseudohomo2 = pseudohomo2[mask]
# mask2 = pseudohomo2.duplicated(['Pinyin2'],keep = False)
# pseudohomo2 = pseudohomo2[~mask2]
# pseudohomo2.shape[0]
#先找出所有的组合，共2375组；
# pseudohomo2.groupby('Pinyin').apply(
#     lambda d: tuple(d.index) if len(d.index) > 1 else None
# ).dropna()
dict = {k: tuple(d.index) for k, d in pseudohomo2.groupby('Pinyin') if len(d) > 1}
len(dict)

list = []
for index, row in newdf_2.iterrows():
    for i in newdf_3.index:
        if newdf_3.get_value(i, 'Pinyin3') == row['Pinyin3']:
            print(i)
            continue

#找出其中只含有二声和三声替换的组合，共组
Dict = {}
for key, value in dict.items():
    if pseudohomo2.at[value[0], 'C1Tone'] == pseudohomo2.at[value[1], 'C1Tone']:
        if (pseudohomo2.at[value[0], 'C2Tone'] == (2 or 3)) and (pseudohomo2.at[value[1], 'C2Tone'] == (2 or 3)):
            Dict.update({key: (value[0], value[1])})
    elif (pseudohomo2.at[value[0], 'C1Tone'] == (2 or 3)) and (pseudohomo2.at[value[1], 'C1Tone']  == (2 or 3)):
        Dict.update({key: (value[0], value[1])})

#打印出这些组合
for key, value in Dict.items():
    print(key, pseudohomo2.at[value[0], 'Word'], pseudohomo2.at[value[1], 'Word'])


# #筛选出pseudo-homophones，保存成一个新的dataframe
# 先去掉音节不重复的词语，因为音节必须相同
mask = newdf.duplicated(['Pinyin'],keep = False)
newdf_1 = newdf[mask]

# 然后把二声都变成三声
newdf_1['Pinyin3'] = newdf_1['Pinyin2'].replace('2', '3', regex=True)
newdf_1

# 取出变化的rows
newdf_2 = newdf_1.loc[newdf_1['Pinyin2'] != newdf_1['Pinyin3']]
newdf_2

# 取出没有变化的rows
newdf_3 = newdf_1.loc[newdf_1['Pinyin2'] == newdf_1['Pinyin3']]
newdf_3

#将变化的rows匹配没有变化的rows
Dict = {}
for index, row in newdf_2.iterrows():
    for i in range(-20, 20):
        if (index+i) in range(1, len(newdf) + 1):
            try:
                if row['Pinyin3'] == newdf_3.get_value(index+i, 'Pinyin3'):
                    Dict.update({index+i: index})
            except: continue

#将字典放进一个不重复的列表
list = []
for key, value in Dict.items():
    if key not in list:
        list.append(key)
    if value not in list:
        list.append(value)

#取出列表的rows，形成新的dataframe
newdf_4 = newdf_1[newdf_1.index.isin(list)]

#给新的dataframe排序，保存到文件中
newdf_4.sort_values(by=['Length', 'Pinyin', 'Frequency'], ascending=[True, True, False], inplace=True)
newdf_4.index = range(1, len(newdf_4) + 1)
newdf_4.to_csv ('newList_4.csv', header=True)
