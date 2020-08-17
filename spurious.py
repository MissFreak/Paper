pseudo-homophones.py
---------------------------------------------------------------
# 把newdf二声都变成三声
newdf['Pinyin3'] = newdf['Pinyin2'].replace('2', '3', regex=True)

# 第一步：把双音节词和三、四音节词分开
spurdf = newdf[newdf['Length'] == 2]
# spurdf.shape[0] 得到22364个
spurdf_1 = newdf[newdf['Length'] == (3 or 4)]
# spurdf_1.shape[0] 得到5557个

# 第二步：去掉spurdf中没有变化的words
# 去掉没有变化的words
spurdf_2 = spurdf[newdf['Pinyin2'] != newdf['Pinyin3']]

# 第三步：把这些nonwords放进三、四音节词匹配,得到新的dataframe

# 先新建一个empty dataframe spurdf_3
spurdf_3 = pd.DataFrame(columns = spurdf_1.columns)
# 然后匹配，得到新的dataframe和spurdf_2的index，放进spurdf_3
spurdf_3 = pd.DataFrame(columns = spurdf_1.columns)
for index, row in spurdf_2.iterrows():
    ex = row['Pinyin3']
    filter = spurdf_1['Pinyin2'].str.contains('(^|\d)' +str(ex), regex=True)
    data = spurdf_1[filter]
    if not data.empty:
        spurdf_3  = pd.concat([spurdf_3, spurdf_2.loc[[index]], data])

spurdf_3.to_csv ('spurdf_3.csv', header=True)

-------------------------------------------------------------------
# 重复三字的情况

# 把newdf二声都变成三声
newdf['Pinyin3'] = newdf['Pinyin2'].replace('2', '3', regex=True)

# 第一步：把三音节词和四音节词分开
spurdf = newdf[newdf['Length'] == 3]
# spurdf.shape[0] 得到22364个
spurdf_1 = newdf[newdf['Length'] == 4]
# spurdf_1.shape[0] 得到5557个

# 第二步：把双音节词中二声的词都变成三声，看有多少nonwords(这些词不出现在pseudo的List中)
pseudo = newdf_1[newdf_1.index.isin(List)]
pseudo = pseudo[pseudo['Length'] == 3] #直接取出pseudo的List中的三音节词
spurdf_2 = spurdf[~spurdf.index.isin(pseudo.index)] #得到nonwords和没有变化的words
# 去掉没有变化的words，先取出变化的rows newdf_2
newdf_2 = newdf.loc[newdf['Pinyin2'] == newdf['Pinyin3']]
# 然后去掉newdf_2，得到13427个词在spurdf_2
spurdf_2 = spurdf_2[~spurdf_2.index.isin(newdf_2.index)]

# 第三步：把这些nonwords放进三、四音节词匹配,得到新的dataframe

# 先新建一个empty dataframe spurdf_3
spurdf_3 = pd.DataFrame(columns = spurdf_1.columns)
# 然后匹配，得到新的dataframe和spurdf_2的index，放进spurdf_3
spurdf_3 = pd.DataFrame(columns = spurdf_1.columns)
for index, row in spurdf_2.iterrows():
    ex = row['Pinyin3']
    filter = spurdf_1['Pinyin2'].str.contains('(^|\d)' +str(ex), regex=True)
    data = spurdf_1[filter]
    if not data.empty:
        spurdf_3  = pd.concat([spurdf_3, spurdf_2.loc[[index]], data])

spurdf_3.to_csv ('spurdf_4.csv', header=True)
