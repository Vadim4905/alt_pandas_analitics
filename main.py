import pandas as pd

import matplotlib.pyplot as plt



df = pd.read_csv('GoogleApps.csv')

# print(df.describe())
# print(df.info())
print(df[df['Rating']>4.9]['Installs'].plot())
df['Size'].head().plot(kind='hist')
plt.show()