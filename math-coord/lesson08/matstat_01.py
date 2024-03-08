import pandas as pd
file_path = 'c:\work\python\math-code\math-coord\lesson08\data.csv'
value_data = pd.read_csv(file_path)
print(value_data.head(10))
# print(value_data.describe())
