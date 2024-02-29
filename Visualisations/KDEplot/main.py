import yfinance as yf
import pandas as pd
import seaborn as sns
from sklearn.preprocessing import MinMaxScaler
import matplotlib.pyplot as plt

# Define the currency pairs
currency_pairs = ['EURUSD=X', 'AUDUSD=X', 'USDJPY=X', 'EURJPY=X', 'AUDJPY=X', 'EURAUD=X']

# Download historical data for the currency pairs and extract just the closing prices.
data = yf.download(currency_pairs, period='2d', interval='1m')
closing_prices = data['Close']

# Normalize the closing prices and convert normalized data to a DataFrame
scaler = MinMaxScaler()
normalized_prices = scaler.fit_transform(closing_prices)
normalized_data = pd.DataFrame(normalized_prices, columns=closing_prices.columns, index=closing_prices.index)

# Plot a joint KDE pair plot to visualize the relationships between the currency pairs over the 2-day period.
sns.pairplot(normalized_data, kind='kde')
plt.show()