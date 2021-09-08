import requests 
#from ta import add_all_ta_features
import pandas as pd
#from ta.momentum import RSIIndicator
#API_key = 'HSJLSMXPLUPA99I5'
#ts  = TimeSeries(key=API_key,output_format = 'pandas')
def pipeline_intraday(ticker):
  params = {
      'access_key' : '43893987de6db8c2ce031c6d3d9db375'
  }
  response = requests.get(f'http://api.marketstack.com/v1/tickers/{ticker}/eod',params)
  response = response.json()
  response = response['data']['eod']
  df1 = pd.DataFrame(response)
  df1.set_index(['date'],inplace=True)
  df1 = df1.iloc[:,0:5]
  df1 = df1.rename(columns={"open":"Open"})
  df1 = df1.rename(columns={"high":"High"})
  df1 = df1.rename(columns={"low":"Low"})
  df1 = df1.rename(columns={"close":"Close"})
  df1 = df1.rename(columns={"volume":"Volume"})
  df1.index = pd.to_datetime(df1.index)
  df1 = df1.sort_index(ascending=True)
  return df1
# More functions for fetching daily data, monthly data and historical data to be updated soon. 
