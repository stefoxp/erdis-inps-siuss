import pandas as pd

def read_csv():
    # read_csv default sep=","
    df = pd.read_csv('data/data.csv', sep=";")

    print(pd.options.display.max_rows)
    print(df.to_string())

def xlsx_to_df(file_path: str, sheet_name_p: str) -> pd:
    return pd.read_excel(file_path, sheet_name=sheet_name_p)

    # print(df.to_string())
    # print(df.head())

if __name__ == '__main__':
    df = xlsx_to_df('data/DSU00081.PS.20210610.0000001_AN_servizi_tracciato_csv.xlsx', 'tracciato')

    print('df.head()', df.head())
    print('df.columns', df.columns)
    print('column A001 ', df['A001 '])
    # print(type(df[['A001 ', 'A100 ']]))
    print('new DataFrame with columns A001 and A100', df[['A001 ', 'A100 ']])
