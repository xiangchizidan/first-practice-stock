import pandas as pd
import numpy as np

file_path = r"D:\Program Files\python练习2\Company (1).csv"

df = pd.read_csv(file_path, encoding='utf-8')

print("=" * 80)
print("原始数据：")
print(df.head())
print(f"\n数据形状: {df.shape}")
print(f"列名: {df.columns.tolist()}")

print("\n" + "=" * 80)
print("任务1：筛选年龄不超过40岁且部门为Dairy或Bakery的男性")
print("=" * 80)

condition1 = (df['Age'] <= 40) & (df['Department'].isin(['Dairy', 'Bakery'])) & (df['Gender'] == 'M')

print("\n方法1：使用 query")
result1_query = df.query("Age <= 40 and Department in ['Dairy', 'Bakery'] and Gender == 'M'")
print(result1_query)

print("\n方法2：使用 loc")
result1_loc = df.loc[(df['Age'] <= 40) & (df['Department'].isin(['Dairy', 'Bakery'])) & (df['Gender'] == 'M')]
print(result1_loc)

print("\n" + "=" * 80)
print("任务2：选出员工ID为奇数所在行的第1、第3和倒数第2列")
print("=" * 80)

df_id_column = df.iloc[:, 0]
odd_mask = df_id_column % 2 == 1
odd_indices = df[odd_mask].index

col1_idx = 0
col3_idx = 2
col_last2_idx = df.shape[1] - 2

print(f"\n选中的列索引: {col1_idx}, {col3_idx}, {col_last2_idx}")
print(f"对应的列名: {df.columns[col1_idx]}, {df.columns[col3_idx]}, {df.columns[col_last2_idx]}")

result2 = df.loc[odd_indices, [df.columns[col1_idx], df.columns[col3_idx], df.columns[col_last2_idx]]]
print(result2)

print("\n" + "=" * 80)
print("任务3：多层索引操作")
print("=" * 80)

df_original = df.copy()
original_columns = df.columns.tolist()

print("\n步骤1：把后三列设为索引")
df_idx = df.set_index(df.columns[-3:].tolist())
print(df_idx)
print(f"索引名称: {df_idx.index.names}")

print("\n步骤2：交换内外两层（交换第0层和第2层）")
df_idx = df_idx.swaplevel(0, 2)
print(df_idx)
print(f"索引名称: {df_idx.index.names}")

print("\n步骤3：恢复中间层索引")
df_idx = df_idx.reset_index(level=1)
print(df_idx)
print(f"索引名称: {df_idx.index.names}")
print(f"列: {df_idx.columns.tolist()}")

print("\n步骤4：修改外层索引名为 Gender")
df_idx.index.name = 'Gender'
print(df_idx)

print("\n步骤5：用下划线合并两层行索引")
if isinstance(df_idx.index, pd.MultiIndex):
    df_idx = df_idx.reset_index()
else:
    df_idx = df_idx.reset_index()

if 'Gender' in df_idx.columns and df_idx.index.name:
    df_idx['combined_index'] = df_idx[df_idx.index.name].astype(str) + '_' + df_idx['Gender'].astype(str)
else:
    level_names = [col for col in df_idx.columns if col in df.columns[-3:]]
    if len(level_names) >= 2:
        df_idx['combined_index'] = df_idx[level_names[0]].astype(str) + '_' + df_idx[level_names[1]].astype(str)

print(df_idx)

print("\n步骤6：把行索引拆分为原状态")
if 'combined_index' in df_idx.columns:
    df_idx[['index1', 'index2']] = df_idx['combined_index'].str.split('_', expand=True)
    df_idx = df_idx.drop('combined_index', axis=1)

print(df_idx)

print("\n步骤7：修改索引名为原表名称")
print(f"原表列名: {original_columns}")

print("\n步骤8：恢复默认索引并将列保持为原表的相对位置")
df_restored = df_idx.reset_index(drop=True)

kept_columns = [col for col in df_restored.columns if col in original_columns]
other_columns = [col for col in df_restored.columns if col not in original_columns]

df_restored = df_restored[kept_columns + other_columns]
print(df_restored)

print("\n" + "=" * 80)
print("任务完成！")
print("=" * 80)
