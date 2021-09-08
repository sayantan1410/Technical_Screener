from Indicator_functions import SMA,EMA,RSI
from backtesting import Strategy
from backtesting.lib import crossover

class SmaCross(Strategy):
    # Define the two MA lags as *class variables*
    # for later optimization
    n1 = 10
    n2 = 20
    
    def init(self):
        # Precompute the two moving averages
        self.sma1 = self.I(SMA, self.data.Close, self.n1)
        self.sma2 = self.I(SMA, self.data.Close, self.n2)
    
    def next(self):
        # If sma1 crosses above sma2, close any existing
        # short trades, and buy the asset
        if ( crossover(self.sma1, self.data.Close) and crossover(self.sma2,self.data.Close)):
            self.position.close()
            self.buy()

        # Else, if sma1 crosses below sma2, close any existing
        # long trades, and sell the asset
        elif (crossover(self.data.Close,self.sma1) and crossover(self.data.Close,self.sma2)):
            self.position.close()
            self.sell()

class SmaxCrossSmay(Strategy):
    # Define the two MA lags as *class variables*
    # for later optimization
    n1 = 10
    n2 = 20
    
    def init(self):
        # Precompute the two moving averages
        self.sma1 = self.I(SMA, self.data.Close, self.n1)
        self.sma2 = self.I(SMA, self.data.Close, self.n2)
    
    def next(self):
        # If sma1 crosses above sma2, close any existing
        # short trades, and buy the asset
        if crossover(self.sma1, self.sma2):
            self.position.close()
            self.buy()

        # Else, if sma1 crosses below sma2, close any existing
        # long trades, and sell the asset
        elif crossover(self.sma2, self.sma1):
            self.position.close()
            self.sell()

class SmaCrossthree(Strategy):
    # Define the two MA lags as *class variables*
    # for later optimization
    n1 = 10
    n2 = 20
    n3 = 30
    
    def init(self):
        # Precompute the two moving averages
        self.sma1 = self.I(SMA, self.data.Close, self.n1)
        self.sma2 = self.I(SMA, self.data.Close, self.n2)
        self.sma3 = self.I(SMA, self.data.Close, self.n3)

    
    def next(self):
        # If sma1 crosses above sma2, close any existing
        # short trades, and buy the asset
        if (crossover(self.sma1, self.data.Close) and crossover(self.sma2,self.data.Close) and crossover(self.sma3,self.data.Close)):
            self.position.close()
            self.buy()

        # Else, if sma1 crosses below sma2, close any existing
        # long trades, and sell the asset
        elif (crossover(self.data.Close, self.sma1) and crossover(self.data.Close,self.sma2) and crossover(self.data.Close,self.sma3)):
            self.position.close()
            self.sell()

class EMASMASMA(Strategy):
    # Define the two MA lags as *class variables*
    # for later optimization
    n1 = 15
    n2 = 20
    n3 = 30
    
    def init(self):
        # Precompute the two moving averages
        self.ema = self.I(EMA, self.data.Close, self.n1)
        self.sma2 = self.I(SMA, self.data.Close, self.n2)
        self.sma3 = self.I(SMA, self.data.Close, self.n3)

    
    def next(self):
        # If sma1 crosses above sma2, close any existing
        # short trades, and buy the asset
        if (crossover(self.ema, self.data.Close) and crossover(self.sma2,self.data.Close) and crossover(self.sma3,self.data.Close)):
            self.position.close()
            self.buy()

        # Else, if sma1 crosses below sma2, close any existing
        # long trades, and sell the asset
        elif (crossover(self.data.Close, self.ema) and crossover(self.data.Close,self.sma2) and crossover(self.data.Close,self.sma3)):
            self.position.close()
            self.sell()

class EMAEMASMA(Strategy):
    # Define the two MA lags as *class variables*
    # for later optimization
    n1 = 5
    n2 = 10
    n3 = 30
    
    def init(self):
        # Precompute the two moving averages
        self.ema = self.I(EMA, self.data.Close, self.n1)
        self.sma2 = self.I(EMA, self.data.Close, self.n2)
        self.sma3 = self.I(SMA, self.data.Close, self.n3)

    
    def next(self):
        # If sma1 crosses above sma2, close any existing
        # short trades, and buy the asset
        if (crossover(self.ema, self.data.Close) and crossover(self.sma2,self.data.Close) and crossover(self.sma3,self.data.Close)):
            self.position.close()
            self.buy()

        # Else, if sma1 crosses below sma2, close any existing
        # long trades, and sell the asset
        elif (crossover(self.data.Close, self.ema) and crossover(self.data.Close,self.sma2) and crossover(self.data.Close,self.sma3)):
            self.position.close()
            self.sell()

class EMAEMAEMA(Strategy):
    # Define the two MA lags as *class variables*
    # for later optimization
    n1 = 5
    n2 = 10
    n3 = 30
    
    def init(self):
        # Precompute the two moving averages
        self.ema = self.I(EMA, self.data.Close, self.n1)
        self.ema1 = self.I(EMA, self.data.Close, self.n2)
        self.ema2 = self.I(EMA, self.data.Close, self.n3)

    
    def next(self):
        # If sma1 crosses above sma2, close any existing
        # short trades, and buy the asset
        if (crossover(self.ema, self.data.Close) and crossover(self.ema1,self.data.Close) and crossover(self.ema2,self.data.Close)):
            self.position.close()
            self.buy()

        # Else, if sma1 crosses below sma2, close any existing
        # long trades, and sell the asset
        elif (crossover(self.data.Close, self.ema) and crossover(self.data.Close,self.ema1) and crossover(self.data.Close,self.ema2)):
            self.position.close()
            self.sell()

class EMASMARSI(Strategy):
    d_rsi = 30  # Daily RSI lookback periods
    w_rsi = 30  # Weekly
    level = 70
    
    def init(self):
        # Compute moving averages the strategy demands
        self.ma10 = self.I(SMA, self.data.Close, 10)
        self.ma20 = self.I(SMA, self.data.Close, 20)
        self.ma50 = self.I(SMA, self.data.Close, 50)
        self.ma100 = self.I(SMA, self.data.Close, 100)
        
        # Compute daily RSI(30)
        self.daily_rsi = self.I(RSI, self.data.Close, self.d_rsi)
        
    def next(self):
        price = self.data.Close[-1]
        
        # If we don't already have a position, and
        # if all conditions are satisfied, enter long.
        if (not self.position and
            self.daily_rsi[-1] > self.level and  
            self.ma10[-1] > self.ma20[-1] > self.ma50[-1] > self.ma100[-1] and
            price > self.ma10[-1]):
            
            # Buy at market price on next open, but do
            # set 8% fixed stop loss.
            self.buy(sl=.92 * price)
        
        # If the price closes 2% or more below 10-day MA
        # close the position, if any.
        elif price < .98 * self.ma10[-1]:
            self.position.close()

class EMASMA_dual(Strategy):
    # Define the two MA lags as *class variables*
    # for later optimization
    n1 = 5
    n2 = 20
    n3 = 30
    n4 = 40
    
    def init(self):
        # Precompute the two moving averages
        self.ema1 = self.I(EMA, self.data.Close, self.n1)
        self.sma1 = self.I(SMA, self.data.Close, self.n2)
        self.sma2 = self.I(SMA, self.data.Close, self.n3)
        self.sma3 = self.I(SMA, self.data.Close, self.n4)

    
    def next(self):
        # sma2 crosses above sma3
        # sma2 crosses close
        # sma3 crosses close
        # ema crosses close
        if (crossover(self.sma2,self.sma3) and crossover(self.sma3,self.ema1) and crossover(self.sma1,self.ema1) and crossover(self.sma2,self.ema1)):
            self.position.close()
            self.buy()

        # Else, if sma1 crosses below sma2, close any existing
        # long trades, and sell the asset
        elif (crossover(self.data.Close, self.ema1) and crossover(self.data.Close,self.sma2) and crossover(self.data.Close,self.sma3)):
            self.position.close()
            self.sell()