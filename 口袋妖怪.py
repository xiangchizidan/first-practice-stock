import pandas as pd
import os
os.chdir(r'D:\Program Files\python练习2')
df = pd.read_csv('Pokemon (1).csv')

stats = ['HP', 'Attack', 'Defense', 'Sp. Atk', 'Sp. Def', 'Speed']

print("1. Total值验证:", (df[stats].sum(axis=1) == df['Total']).all())

df = df.drop_duplicates(subset=['#'], keep='first')

type1_counts = df['Type 1'].value_counts()
print(f"\n2. 第一属性种类: {len(type1_counts)}, 前三:\n{type1_counts.head(3)}")

combos = df['Type 1'] + '/' + df['Type 2'].fillna('None')
print(f"\n3. 属性组合种类: {combos.nunique()}")

type1_list = df['Type 1'].unique()
type2_list = df['Type 2'].dropna().unique()
all_combos = {f"{t1}/{t2}" for t1 in type1_list for t2 in type2_list if t1 != t2}

actual_combos = set(combos[df['Type 2'].notna()].values)

print(f"\n4. 尚未出现的属性组合: {len(all_combos - actual_combos)}")

attack_class = df['Attack'].apply(lambda x: 'high' if x > 120 else ('low' if x < 50 else 'mid'))
print(f"\n5. 物攻分类:\n{attack_class.value_counts()}")

print(f"\n6. 两种大写方法结果一致: {df['Type 1'].str.upper().equals(df['Type 1'].apply(str.upper))}")

df['Deviation'] = df[stats].apply(lambda row: max(abs(v - row.median()) for v in row), axis=1)
print(f"\n7. 离差最大的前10个妖怪:\n{df.nlargest(10, 'Deviation')[['Name', 'Deviation']]}")

