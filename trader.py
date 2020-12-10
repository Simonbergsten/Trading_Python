"""
Credit to the youtube channel Part Time Larry
"""

import backtrader
import datetime
from strategies import TestStrategy
# https://www.backtrader.com/docu/


cerebro = backtrader.Cerebro() # Instantiate the session

cerebro.broker.set_cash(10000) # Set cash value

data = backtrader.feeds.YahooFinanceCSVData(
    dataname = 'oracle.csv',
    fromdate = datetime.datetime(2000, 1, 1),
    todate = datetime.datetime(2020, 1, 1),
    reverse = False)


cerebro.adddata(data) # Add the data to the object
cerebro.addstrategy(TestStrategy)
cerebro.addsizer(backtrader.sizers.FixedSize, stake = 1000)




# Testing it's working
print("Starting portfolio value: %.2f" % cerebro.broker.getvalue())
cerebro.run()
print("Final portfolio value: %.2f" % cerebro.broker.getvalue())

# cerebro.plot()
