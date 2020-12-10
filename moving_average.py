"""
Credit to the youtube channel Part Time Larry
"""


def getdata(days = 50):
    with open('oracle.csv') as f:
        return f.readlines()[-days:]


def moving_average(n_days):
    closing_price_sum = 0
    data = getdata(n_days)
    for line in data:
        splitted_line = line.split(",")
        close = splitted_line[4]
        closing_price_sum += float(close)

    print(closing_price_sum/n_days)

moving_average(200)