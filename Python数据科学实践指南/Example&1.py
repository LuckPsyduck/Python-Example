
import pandas as pd
import numpy as np
a = pd.Series([1, 0.3, np.nan])
b = pd.Series(np.array([1, 2, 3]))

c = pd.Series([1, 2, 3], index = ['a', 'b', 'c'])

data = pd.date_range('20160101', periods = 5)

df = pd.DataFrame(np.random.randn(5, 4), index = date, columns = list("ABCD"))
print(df)

df.head()
df.tail()
df.index
df.columns
df.values
df.describe
df.T
df.sort_values(by='D')


df['A']
df[1:3]
