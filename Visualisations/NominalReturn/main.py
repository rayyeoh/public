import yfinance as yf
import plotly.graph_objects as go
from time import strftime

# Define the symbols for the currency pairs and indices
symbols = ['EURUSD=X', 'USDJPY=X', 'AUDUSD=X', '^GSPC', '^IXIC', '^N225', '^HSI', '^FTSE', '^STOXX50E', '^DJI','CL=F', 'HG=F', 'BTC-USD', 'ETH-USD', 'ZB=F', 'ZN=F', 'ZT=F', 'CC=F']
data = yf.download(symbols, period='1mo')

closings = data['Close'].dropna()
returns = ((closings.iloc[-1] / closings.iloc[0] - 1)*100).sort_values(ascending=False)
range = closings.index[0].strftime("%Y-%m-%d") + ' -> ' + closings.index[-1].strftime("%Y-%m-%d")
textvalue = [f'{round(x, 2)}%' for x in returns.values]

fig = go.Figure()
fig.add_trace(go.Bar(x=returns.index, y=returns.values, marker=dict(color=returns.values, colorscale='RdYlGn'), textposition='auto', text=textvalue))
fig.update_layout(title=f'Nominal Returns calculated between {range}', xaxis_title='Symbol', yaxis_title='%')
fig.show()