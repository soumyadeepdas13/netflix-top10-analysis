import pandas as pd

df = pd.read_excel("Data File.xlsx", sheet_name="NFLX Top 10")
print(df.head())
