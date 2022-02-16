import pandas

ar=[1,1,1,1,2,2,2,3,3,4]
df=pandas.DataFrame({'key':ar,'data':range(len(ar))},columns=['key','data'])
g = df.groupby('key')
print(g.head())