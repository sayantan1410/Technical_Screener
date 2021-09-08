def nifty_50():
  """Returns a dataframe with the top 50 companies in the nifty index at the time the function is called"""
  
  url = 'https://archives.nseindia.com/content/indices/ind_nifty50list.csv'
  response = requests.get(url).content
  df = pd.read_csv(io.StringIO(response.decode('utf-8')))
  return df