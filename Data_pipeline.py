import requests 
#from ta import add_all_ta_features
import pandas as pd
def pipeline_intraday(ticker):
  params = {
      'access_key' : '0f6a05295cb99df83172b6be1676f7e7',
      'limit' : '3000'
  }
  response = requests.get(f'http://api.marketstack.com/v1/tickers/{ticker}/intraday',params)
  response = response.json()
  response = response['data']['intraday']
  df1 = pd.DataFrame(response)
  df1.set_index(['date'],inplace=True)
  df1 = df1.iloc[:,0:5]
  df1 = df1.rename(columns={"open":"Open"})
  df1 = df1.rename(columns={"high":"High"})
  df1 = df1.rename(columns={"low":"Low"})
  df1 = df1.rename(columns={"close":"Close"})
  df1 = df1.rename(columns={"volume":"Volume"})
  if (df1.isnull().values.any() == True):
    df1.dropna(axis = 0,inplace=True)
  df1 = df1.sort_index(ascending=True)
  df1.index = pd.to_datetime(df1.index)
  return df1
# More functions for fetching daily data, monthly data and historical data to be updated soon. 
