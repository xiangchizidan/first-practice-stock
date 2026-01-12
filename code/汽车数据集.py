import pandas as pd
import numpy as np

df = pd.read_csv('car (1).csv')

print("="*60)
print("1. 过滤Country数超过2个的汽车，计算按Country分组的统计")
print("="*60)
country_counts = df['Country'].value_counts()
valid_countries = country_counts[country_counts > 2].index
df_filtered = df[df['Country'].isin(valid_countries)]

country_stats = df_filtered.groupby('Country')['Price'].agg([
    ('price_mean', 'mean'),
    ('price_std', 'std'),
    ('count', 'size')
])
country_stats['CoV'] = country_stats['price_std'] / country_stats['price_mean']
country_stats = country_stats.drop('price_std', axis=1)

print(country_stats)
print()

print("="*60)
print("2. 按表中位置的三分之一分组，统计Price均值")
print("="*60)
n = len(df)
third = n // 3

df['position_group'] = pd.cut(range(n), bins=[0, third, 2*third, n],
                               labels=['First Third', 'Middle Third', 'Last Third'],
                               include_lowest=True)
position_price_mean = df.groupby('position_group')['Price'].mean()

print(position_price_mean)
print()

print("="*60)
print("3. 按Type分组，计算Price和HP的最大值和最小值")
print("="*60)
type_agg = df.groupby('Type').agg({
    'Price': ['max', 'min'],
    'HP': ['max', 'min']
})
type_agg.columns = ['_'.join(col).strip() for col in type_agg.columns.values]

print(type_agg)
print()

print("="*60)
print("4. 按Type分组，对HP进行min-max归一化")
print("="*60)
def minmax_normalize(group):
    return (group - group.min()) / (group.max() - group.min())

df['HP_normalized'] = df.groupby('Type')['HP'].transform(minmax_normalize)
print(df[['Type', 'HP', 'HP_normalized']].head(10))
print()

print("="*60)
print("5. 按Type分组，计算Disp与HP的相关系数")
print("="*60)
correlations = df.groupby('Type').apply(
    lambda x: x['Disp'].corr(x['HP'])
)
print(correlations)
