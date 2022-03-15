import pandas as pd 
df = pd.read_csv('merged.csv')
del df['Luminosity']
df.to_csv('result.csv')