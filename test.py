import pandas as  pd
import sqlite3

import pandas as pd
import matplotlib.pyplot as plt
s = pd.Series(data = [10, 5, 15, 20, 10],
index = [1, 2, 3, 4, 5])
# s.plot()
# plt.show()
# x= [1,2,3,4]
# y = [1,5,2,4]
# plt.plot(x,y,'r--*')
# plt.show()


# conn = sqlite3.connect("city_data.db")
# df = pd.read_sql("SELECT * FROM cities", conn)

# df.info()
df = pd.read_csv('GooglePlayStore_wild.csv')

# df_family =df[df['Category'] == 'FAMILY']
# df_art_design = df[df['Category'] == 'ART_AND_DESIGN']
# print(df_family)
# print(df_art_design)

# print(df.groupby(by ='Category')['Installs'].agg(['min','max']))


# df_content_rating = df['Content Rating'].value_counts()

# print(round(df_content_rating['Teen'] / df_content_rating['Everyone 10+'],2))

# df_new = df.groupby(by ='Type')['Rating'].mean()


# print(df_new['Paid'] - df_new['Free'])

# print(df.groupby(by ='Category')['Size'].agg(['min','max'])['COMICS'])

# df_finance = df[df['Category'] == 'FINANCE' ]
# print(len(df_finance[df_finance['Rating'] > 4.5]))

# df_free = df[(df['Type'] == 'Free') & (df['Category'] == 'GAME')]
# df_paid = df[(df['Type'] == 'Paid') & (df['Category'] == 'GAME')]

# print(    len(df_free[df_free['Rating'] > 4.9])  / len(df_paid[df_paid['Rating'] > 4.9]))

# temp = df.groupby(by = 'Type')['Rating'].agg(['min','mean','max'])



# def find_max(d):
#     max_num = max(list(d.values()))
#     for k in d:
#         if d[k] == max_num:
#             return k

# temp = df.groupby(by = ['Category','Content Rating'])['Reviews'].agg(['mean'])

# print(find_max(dict(temp['mean']['EDUCATION'])))
# print(find_max(dict(temp['mean']['FAMILY'])))
# print(find_max(dict(temp['mean']['GAME'])))

# def find_any_age(d):
#     res= []
#     repeat = 1
#     before = ''
#     for k in d:
#         if before == k[0]:
#             repeat += 1
#             if repeat == 3:
#                 res.append(k[0])
#         else:
#             repeat = 1
#         before = k[0]

#     return res

#
# temp = df_paid.groupby(by = ['Category','Content Rating'])['Reviews'].agg(['mean'])

# print(find_any_age(dict(temp['mean'])))

 
# df_free = df[df['Type'] == 'Free']
# # temp = df_free.groupby(by = ['Category','Content Rating'])['Reviews'].agg(['mean'])
# temp = df_free.pivot_table(columns = 'Content Rating',
#                     index = 'Category',
#                     values = 'Reviews',
#                     aggfunc = 'mean')

# print(dict(dict(temp)['Everyone']))

# print(df.isnull())

# df['Rating'].fillna(0,inplce=True)

# df = df.dropna()
# df.info()
# def foo(a):
#     pass


# print(df['Size'].apply(foo))








# df['Profit'] = df['Price'] *df['Installs']

def size_format(size):
    if size == 'Varies with device':
        return 0
    elif size.endswith('K'):
        return float(size.replace('K','')) / 1024
    elif size.endswith('M'):
        return float(size.replace('M',''))
df['Size'] = df['Size'].apply(size_format)     

# group = df.groupby(by='Category')['Size'].max()

# print(group['TOOLS'])








def get_installs(size:str):
    if size.endswith('+'):
        size = size.replace('+','')
    return int(size.replace(',',''))

df['Installs'] = df['Installs'].apply(get_installs) 

# group = df.groupby(by=['Type','Content Rating'])['Installs'].mean()
# print(group)

# df_cur = df[pd.isnull(df['Type'])]
# print(df_cur['App'])
# print(df_cur['Price'])


def price_format(price:str):
    price = price.replace('$','')
    return float(price)

df['Price'] = df['Price'].apply(price_format)



df['Profit']= df['Installs'] * df['Price']

# print(df[df['Type'] == 'Paid']['Profit'].max())


def count_genres(data):
    data = data.split(';')
    return len(data)

df['Num_genres'] = df['Genres'].apply(count_genres)

# print(df['Num_genres'].max())

def get_seasons(data):
    seasons ={'Winter':['January','February','December'],
              'Summer': ['June','July','August'],
              'Spring':['March','April','May',],
              'Autumn':['September','October','November']}

    for season in seasons:
        if data.split(' ',1)[0] in seasons[season]:
            return season



df['Season'] = df['Last Updated'].apply(get_seasons)
# print(df['Season'].value_counts())



df['Type'].value_counts().plot(kind='pie')
plt.show()