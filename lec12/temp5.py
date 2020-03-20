import pandas 

d = {
    'a': (1, 101),
    'b': (2, 202),
    'c': (3, 303)
}

df = pandas.DataFrame.from_dict(d)
df.plot()
df.to_csv('data.csv')

df1 = pandas.read_csv('data.csv')