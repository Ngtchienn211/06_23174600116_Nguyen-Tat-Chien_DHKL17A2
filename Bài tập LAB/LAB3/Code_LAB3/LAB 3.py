import pandas as pd

"""LAB 3.1"""
stocks1 = pd.read_csv(r"E:\python_nang_cao\Bài tập LAB\LAB3\DATA_LAB3\stocks1.csv")

print("5 dòng đầu tiên của stocks1:")
print(stocks1.head())
print("\nKiểu dữ liệu của mỗi cột:")
print(stocks1.dtypes)
print("\nThông tin tổng quan của stocks1:")
print(stocks1.info())

"""LAB 3.2"""
print("\nKiểm tra dữ liệu Null:")
print("\nKiểm tra dữ liệu Null:")
print(stocks1.isnull().sum())

stocks1['high'].fillna(stocks1['high'].mean(), inplace=True)
stocks1['low'].fillna(stocks1['low'].mean(), inplace=True)

print("\nThông tin sau khi xử lý Null:")
print(stocks1.info())

"""LAB 3.3"""
stocks2 = pd.read_csv(r"E:\python_nang_cao\Bài tập LAB\LAB3\DATA_LAB3\stocks2.csv")
stocks = pd.concat([stocks1, stocks2])
gia_tb = stocks.groupby('date')[['open', 'high', 'low', 'close']].mean()
print(gia_tb.head())

"""LAB 3.4"""
companies = pd.read_csv(r"E:\python_nang_cao\Bài tập LAB\LAB3\DATA_LAB3\companies.csv")
print(companies.head())
merge_data = pd.merge(stocks, companies, left_on='symbol', right_on='name', how='inner')
gia_dong_cua_tb = merge_data.groupby('symbol')['close'].mean()
print(gia_dong_cua_tb.head())

"""LAB 3.5"""
stocks.set_index(['date', 'symbol'], inplace=True)
grouped_data = stocks.groupby(['date', 'symbol']).mean()
grouped_data.sort_index(inplace=True)
print(grouped_data.head(5))

"""LAB 3.6"""
pivot_table = stocks.reset_index().pivot_table(index='date', columns='symbol', values='close', aggfunc='mean')
pivot_table['Total Volume'] = stocks.groupby('symbol')['volume'].sum()
pivot_table = pivot_table.sort_values(by='Total Volume', ascending=False)
print(f"\npivot_table.head(5)")
