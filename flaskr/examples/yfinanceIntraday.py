import yfinance as yf
intraday_data = yf.download(tickers="MSFT",
                            period = '5d',
                            interval= "1d",
                            auto_adjust=True
                            actions=True)
intraday_data.head()
print(intraday_data)

