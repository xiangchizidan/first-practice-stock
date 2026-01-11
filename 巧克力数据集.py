import pandas as pd
import numpy as np

df = pd.read_csv('chocolate (1).csv')

print("原始数据信息:")
print(f"数据形状: {df.shape}")
print(f"列名: {df.columns.tolist()}")
print("\n前5行:")
print(df.head())

print("\n" + "="*80)
print("操作1: 把列索引名中的 \\n 替换为空格")
print("="*80)
df.columns = df.columns.str.replace('\n', ' ')
print(f"更新后的列名: {df.columns.tolist()}")
print(df.head())

print("\n" + "="*80)
print("操作2: Rating 2.75分及以下且Cocoa Percent高于中位数的样本")
print("="*80)
cocoa_median = df['Cocoa Percent'].median()
print(f"Cocoa Percent中位数: {cocoa_median}")

condition2 = (df['Rating'] <= 2.75) & (df['Cocoa Percent'] > cocoa_median)
result2 = df[condition2]
print(f"满足条件的样本数: {len(result2)}")
print("\n满足条件的样本:")
print(result2)

print("\n" + "="*80)
print("操作3: 按Review Date和Company Location索引，选出2012年后且特定国家的样本")
print("="*80)
df_indexed = df.set_index(['Review Date', 'Company Location'])
print(f"索引后数据形状: {df_indexed.shape}")
print("\n前5行索引:")
print(df_indexed.head())

exclude_locations = ['France', 'Canada', 'Amsterdam', 'Belgium']
condition3 = (df_indexed.index.get_level_values('Review Date') > 2012) & \
             (~df_indexed.index.get_level_values('Company Location').isin(exclude_locations))
result3 = df_indexed[condition3]
print(f"\n满足条件的样本数: {len(result3)}")
print("\n满足条件的样本:")
print(result3)

print("\n" + "="*80)
print("总结")
print("="*80)
print(f"操作1: 列名已更新，\\n 替换为空格")
print(f"操作2: 找到 {len(result2)} 个Rating≤2.75且Cocoa Percent>{cocoa_median}的样本")
print(f"操作3: 找到 {len(result3)} 个Review Date>2012且不在指定国家的样本")
