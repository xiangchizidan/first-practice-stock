import pandas as pd
import os
os.chdir(r'D:\Program Files\python练习2')
df = pd.read_csv('chocolate (1).csv')

df.columns = df.columns.str.replace('\n', ' ')
print("操作1结果:")
print(df.head())

cocoa_median = df['Cocoa Percent'].median()
result2 = df[(df['Rating'] <= 2.75) & (df['Cocoa Percent'] > cocoa_median)]
print("\n操作2结果 (Rating≤2.75且Cocoa Percent>中位数):")
print(result2)

df_indexed = df.set_index(['Review Date', 'Company Location'])
result3 = df_indexed[(df_indexed.index.get_level_values('Review Date') > 2012) &
                     (~df_indexed.index.get_level_values('Company Location').isin(['France', 'Canada', 'Amsterdam', 'Belgium']))]
print("\n操作3结果 (Review Date>2012且不在指定国家):")
print(result3)
