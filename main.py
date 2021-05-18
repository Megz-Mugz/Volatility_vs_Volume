import datetime as dt
import pandas_datareader as web
import seaborn as sns
import matplotlib.pyplot as plt
plt.style.use('dark_background')

# get data
start = dt.datetime(2000, 1, 1)
now = dt.datetime.now()
ticker = input('enter ticker symbol:')
df = web.DataReader(ticker, 'yahoo', start, now)

# create volatility column
df['Volatility'] = abs((df['Adj Close'] - df['Open']) / df['Open'])

# varible assignment
x = df['Volatility']
y = df['Volume']

sns.jointplot(kind='scatter', x=x, y=y, marker='*', color='blue')

plt.show()
