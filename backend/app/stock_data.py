import yfinance as yf

print(yf.Ticker('VOO').get_info().keys())
print(yf.Ticker('VOO').get_info()['regularMarketPrice'])

def get_stock_news(ticker: str):
    ticker_news = yf.Ticker(ticker).news
    news_summaries = [news_data.get('content',[]).get('summary','') for news_data in ticker_news]    
    return news_summaries


def get_stock_price(ticker:str):
    return yf.Ticker(ticker).get_info().get('regularMarketPrice')


print(get_stock_news('VOO'))
print(get_stock_price('VOO'))