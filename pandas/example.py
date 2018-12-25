import pandas as pd
import matplotlib.pyplot as plt

brics = pd.read_csv('brics.csv', index_col=0)

print(brics)
print(brics.info())
print(brics.describe(exclude='object'))

# accessing columns
print(brics['country'])
print(type(brics['country']))
# following way is not recommended as it may conflict with function names
print(brics.country)
# notice the way we access multiple columns
print(brics[['country', 'capital']])
print(type(brics[['country', 'capital']]))

# adding new columns
brics['on_earth'] = [True, True, True, True, True]
brics['density'] = brics['population'] / brics['area'] * 1000000

print(brics)

# accessing rows
print(brics.loc['BR'])
print(brics.loc[['BR', 'SA']])
print(brics.iloc[1:-2])

# accessing elements
print(brics.loc['BR', 'capital'])
print(brics['capital'].loc['BR'])
print(brics.loc['BR']['capital'])

# group by
print(brics.groupby(['country']).describe())
print(brics.groupby(['country']).area.mean())
print(brics.groupby(['country'])['area', 'population'].count())

# plotting by pandas
brics.plot(kind='bar', x='country', y='area')

plt.show()
brics.plot(subplots=True)
plt.show()