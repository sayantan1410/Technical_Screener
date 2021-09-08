import io
from backtesting import Backtest
import backtesting as bt
from Company_data import strategies
from Data_pipeline import pipeline_intraday
import matplotlib.pyplot as plt
import matplotlib as mpl
 
def save_image(data,company):
    image_location = []
    plt.figure(figsize=(6, 4))
    mpl.rcParams['lines.linewidth'] = 2
    mpl.rcParams['lines.linestyle'] = '--'
    fig = plt.plot(data.index,data.Close,)
    plt.xlabel('Time')
    plt.ylabel('Closing Price in USD')
    plt.savefig(f"static/images/{company}.png")
    image_location.append(f"static/images/{company}.png")
    fig.pop(0).remove()

def company_ranking(companies):  
    return_percentage = {}
    for x in companies:
        company = x
        df = pipeline_intraday(x)
        save_image(df,company)
        for keys in strategies:
            bt = Backtest(df,strategies[keys],cash=100000, commission=.002)
            company_strategy = bt.run()
            return_percentage[f'{company}_{keys}'] = company_strategy
    return_array = sorted(return_percentage.items(), key=lambda x: x[1][6], reverse=True)
    return return_array
        
def strategy_backtest(company,strategy):
    x = pipeline_intraday(company)
    bt = Backtest(x,strategies[strategy],cash = 100000,commission = 0.002)
    company_stats = bt.run()
    return company_stats
