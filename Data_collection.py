from Strategy_backtesting import company_ranking
from Company_data import Stocks
print('the file is getting executed')
largeCapReturns = company_ranking(Stocks['Large-Cap Stocks'])
mediumCapReturns = company_ranking(Stocks['Medium-Cap Stocks'])