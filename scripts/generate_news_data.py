import pandas as pd
import random
from datetime import datetime, timedelta

# Stocks you have data for
stocks = ['AAPL', 'AMZN', 'GOOG', 'META', 'MSFT', 'NVDA', 'TSLA']
publishers = ['Bloomberg', 'Reuters', 'CNBC', 'WSJ', 'Yahoo Finance', 'MarketWatch']
headlines_templates = [
    "Analysts upgrade {stock} price target amid strong earnings",
    "{stock} faces regulatory challenges after latest announcement",
    "{stock} shares surge after new product reveal",
    "Investors cautious as {stock} reports quarterly results",
    "{stock} stock hits new 6-month high",
    "{stock} faces market volatility amid sector changes",
    "{stock} announces strategic partnership with tech giant"
]

# Generate random news
data = []
start_date = datetime(2024, 1, 1)
end_date = datetime(2024, 12, 31)

for _ in range(500):  # 500 news articles
    stock = random.choice(stocks)
    headline = random.choice(headlines_templates).format(stock=stock)
    publisher = random.choice(publishers)
    date = start_date + timedelta(days=random.randint(0, (end_date - start_date).days))
    data.append([headline, publisher, date.strftime('%Y-%m-%d'), stock])

# Create DataFrame
df_news = pd.DataFrame(data, columns=['headline', 'publisher', 'date', 'stock'])

# Save to CSV
df_news.to_csv('data/news_data.csv', index=False)
print("Mock news dataset saved to data/news_data.csv")
