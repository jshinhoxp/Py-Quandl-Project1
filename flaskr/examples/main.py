import pandas as pd
import quandl as qd
import matplotlib.pyplot as plt
import numpy as np
import yfinance as yf

start_date = '1990-01-01'
end_date = '2022-01-01'

tickers_list = ['AAPL', 'IBM', 'MSFT', 'WMT']

data = pd.DataFrame(columns=tickers_list)

for ticker in tickers_list:
   data[ticker] = yf.download(ticker, start_date, end_date)['Adj Close']

data.head()
print(data)

data.plot(figsize=(10, 7))

plt.legend()
plt.title("Adjusted Close Price", fontsize=16)

plt.ylabel('Price', fontsize=14)
plt.xlabel('Year', fontsize=14)

plt.grid(which="major", color='k', linestyle='-.', linewidth=0.5)
plt.show()
