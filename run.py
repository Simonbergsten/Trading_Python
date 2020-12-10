"""
Credit to the youtube channel Part Time Larry
"""
import os, sys, argparse
import pandas as pd
import backtrader as bt
from strategies import GoldenCross
from strategies import BuyHold

strategies = {
    "golden_cross":GoldenCross,
    "buy_hold": BuyHold
}

parser = argparse.ArgumentParser()
parser.add_argument("strategy", help="which strategy to run",
                    type = str)
args = parser.parse_args()

if not args.strategy in strategies:
    print(f"Invalid strategy, must be one of {strategies.keys()}")
    sys.exit()

cerebro = bt.Cerebro()
cerebro.broker.set_cash(100000)

oracle_prices = pd.read_csv('oracle.csv', index_col="Date", parse_dates=True)
feed = bt.feeds.PandasData(dataname = oracle_prices)
cerebro.adddata(feed)

cerebro.addstrategy(strategies[args.strategy])
cerebro.run()
# cerebro.plot()

# To run the code
# python3 run.py golden_cross
