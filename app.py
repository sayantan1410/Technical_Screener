from flask import Flask,render_template,request
import pandas as pd
import json
import plotly
import plotly.express as px 
from Data_collection import largeCapReturns,mediumCapReturns
from Company_data import analysis_companies,strategies,outcome_variables,Stocks,Strategy_description
from Data_pipeline import pipeline_intraday
from ta import momentum
from ta import trend
from ta.volatility import BollingerBands
from ta.volume import MFIIndicator
from Strategy_backtesting import company_ranking,strategy_backtest

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html',company = analysis_companies,indices = Stocks,Strategy = strategies)

@app.route('/ranking',methods=['POST'])
def ranking():
    index = request.form.get('index',False)
    stock = Stocks[index]
    if index == 'Large-Cap Stocks':
        return_array = largeCapReturns
    else:
        return_array = mediumCapReturns
    #return_array = company_ranking(stock)
    #image_storage(return_array)
    return render_template('ranking.html',return_array = return_array,outcome_variables = outcome_variables,strategy_description = Strategy_description)

@app.route('/visualization',methods = ['POST'])
def visualizations():
    company  = request.form.get('company', False)
    data = pipeline_intraday(company)
    # Simple Moving Average
    data['SMA10'] = trend.sma_indicator(close = data['Close'], window = 10, fillna = False)

    # Bollinger Bands
    indicator_bb = BollingerBands(close=data["Close"], window=12, window_dev=2)
    data['BB_BBM'] = indicator_bb.bollinger_mavg() # middle band
    #data['BB_BBH'] = indicator_bb.bollinger_hband() # high band
    #data['BB_BBL'] = indicator_bb.bollinger_lband() # low band
    data['MACD'] = trend.macd(close=data["Close"], window_slow = 26, window_fast=12)

    # RSI
    data['RSI'] = momentum.rsi(close=data["Close"], window=12)

    # MFI
    indicator_mfi = MFIIndicator(high=data['High'],low=data['Low'],close=data['Close'],volume=data['Volume'],window=12,fillna=False)
    data['MFI'] = indicator_mfi.money_flow_index()
    closing_price = data.iloc[-1,-9]
    volume = data.iloc[-1,-8]
    df = data.iloc[-11:-1,-5:-1]
    fig = px.line(data, x = data.index, y = ["Close","SMA10"])
    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    return render_template('visualizations.html',
                            closing_price=closing_price,volume = volume,company = company,
                            tables = [df.to_html()],titles = ['SMA','BB_BBM','BB_BBH','BB_BBL','MACD','RSI','MFI'],graphJSON=graphJSON)
    
@app.route('/strategy',methods =['POST'])
def strategy():
    company = request.form.get('company',False)
    strategy = request.form.get('Strategy')
    company_statistics = strategy_backtest(company,strategy)
    return render_template('strategy.html',company = company, strategy = strategy,company_statistics=company_statistics,strategy_description = Strategy_description,outcome_variables=outcome_variables)

@app.route('/description')
def description():
    return render_template('description.html',strategy_description =Strategy_description)

if __name__ == "__main__":
    app.run(debug=True)
