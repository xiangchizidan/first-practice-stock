import pandas as pd
import os
os.chdir(r'D:\Program Files\python练习2')
df = pd.read_csv('Company (1).csv')

#分别只使用 query 和 loc 选出年龄不超过四十岁且工作部门为 Dairy 或 Bakery 的男性。
print("\nquery方法：")
print(df.query("Age <= 40 and Department in ['Dairy', 'Bakery'] and Gender == 'M'"))

print("\nloc方法：")
print(df.loc[(df['Age'] <= 40) & (df['Department'].isin(['Dairy', 'Bakery'])) & (df['Gender'] == 'M')]])

# 选出员工 ID 号 为奇数所在行的第1、第3和倒数第2列。
odd_rows = df[df.iloc[:, 0] % 2 == 1]
cols = [df.columns[0], df.columns[2], df.columns[-2]]
print(odd_rows[cols])

#多层索引操作
df_idx = df.set_index(df.columns[-3:].tolist())
print("\n1. 后三列设为索引后：")
print(df_idx)

df_idx = df_idx.swaplevel(0, 2)
print("\n2. 交换内外两层：")
print(df_idx)

df_idx = df_idx.reset_index(level=1)
print("\n3. 恢复中间层索引：")
print(df_idx)

df_idx.index.name = 'Gender'
print("\n4. 修改外层索引名为 Gender：")
print(df_idx)

df_idx = df_idx.reset_index()
cols_list = df_idx.columns.tolist()
df_idx['combined'] = df_idx[cols_list[0]].astype(str) + '_' + df_idx[cols_list[1]].astype(str)
print("\n5. 下划线合并两层索引：")
print(df_idx)

df_idx[['idx1', 'idx2']] = df_idx['combined'].str.split('_', expand=True)
df_idx = df_idx.drop('combined', axis=1)
print("\n6. 拆分索引：")
print(df_idx)

df_final = df_idx.reset_index(drop=True)
print("\n7-8. 恢复默认索引（保持原列位置）：")
print(df_final)
