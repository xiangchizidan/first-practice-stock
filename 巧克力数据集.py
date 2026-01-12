import pandas as pd
import os
os.chdir(r'D:\Program Files\python练习2')
df = pd.read_csv('chocolate (1).csv')
# 把列索引名中的 \n 替换为空格。
df.columns = df.columns.str.replace('\n', ' ')
print("操作1结果:")
print(df.head())
# 巧克力 Rating 评分为1至5，每0.25分一档，请选出2.75分及以下且可可含量 Cocoa Percent 高于中位数的样本。
cocoa_median = df['Cocoa Percent'].median()
result2 = df[(df['Rating'] <= 2.75) & (df['Cocoa Percent'] > cocoa_median)]
print("\n操作2结果 (Rating≤2.75且Cocoa Percent>中位数):")
print(result2)
# 将 Review Date 和 Company Location 设为索引后，选出 Review Date 在2012年之后且 Company Location 不属于 France, Canada, Amsterdam, Belgium 的样本。
df_indexed = df.set_index(['Review Date', 'Company Location'])
result3 = df_indexed[(df_indexed.index.get_level_values('Review Date') > 2012) &
                     (~df_indexed.index.get_level_values('Company Location').isin(['France', 'Canada', 'Amsterdam', 'Belgium']))]
print("\n操作3结果 (Review Date>2012且不在指定国家):")
print(result3)
