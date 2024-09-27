import pandas as pd

import matplotlib.pyplot as plt



df = pd.read_csv('GoogleApps.csv')

# print(df.describe())
# print(df.info())
# print(df[df['Rating']>4.9]['Installs'].plot())
# df['Size'].head().plot(kind='hist')
# plt.show()

# print(df.groupby(by='Category')['Rating'].mean().plot(kind='pie'))
# plt.show()

ans = input("""Welcome to the dataset analytics!!!
0 - exit
1 - show general statistics about dataset
2 - show the most popular category
3 get your preferance statistic 
: """)

while ans != '0':
    if ans == '1':
        print(df.describe())
    elif ans == '2':
        temp = df.groupby(by='Category')['Installs'].mean()
        print(temp)
        temp.plot(kind='pie')
    elif ans == '3':
        category = input('type in what property would you like to see: ')
        try:
            df[category]
        except:
            continue
        aggfunc = input('type in prefered aggrigation fuction (mean or median): ')
        if aggfunc =='mean':
            temp = df.groupby(by='Category')[category].mean()
        elif aggfunc =='median':
            temp = df.groupby(by='Category')[category].median()
        else:
            continue    
        print(temp)
        temp.plot(kind='pie')
    else:
        print('invalid input, please type in only digits')
        
    plt.show()
    
    ans = input("""Welcome to the dataset analytics!!!
0 - exit
1 - show general statistics about dataset
2 - show the most popular category
3 - get your preferance statistic 
: """)
