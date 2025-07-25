import pandas as pd
import glob
import os

# 1. Load all stock files
stock_files = glob.glob(os.path.join('data', 'yfinance_data', '*_historical_data*.csv'))
dfs_stock = []

for file in stock_files:
    df = pd.read_csv(file)
    stock_name = os.path.basename(file).split('_')[0]  # Extract ticker (e.g., AAPL)
    df['stock'] = stock_name
    df['Date'] = pd.to_datetime(df['Date'])
    dfs_stock.append(df)

df_stocks = pd.concat(dfs_stock, ignore_index=True)

# 2. Load news data
df_news = pd.read_csv('data/news_data.csv')
df_news['date'] = pd.to_datetime(df_news['date'])

# 3. Merge on stock & date
df_merged = pd.merge(
    df_news,
    df_stocks,
    left_on=['stock', 'date'],
    right_on=['stock', 'Date'],
    how='inner'
)
df_merged.drop(columns=['Date'], inplace=True)

# 4. Save merged data
output_path = 'data/merged_stock_news.csv'
df_merged.to_csv(output_path, index=False)
print(f"Merged dataset saved to {output_path}")
print(df_merged.head())
