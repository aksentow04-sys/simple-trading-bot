def strategy(prices):
    if prices[-1] > prices[-2]:
        return "BUY"
    else:
        return "SELL"
