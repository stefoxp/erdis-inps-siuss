import pandas as pd

# read_csv default sep=","
df = pd.read_csv('data/data.csv', sep=";")

print(pd.options.display.max_rows)
print(df.to_string())
