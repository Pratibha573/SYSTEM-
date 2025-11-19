import sys
if len(sys.argv) != 4:
    print("Usage: python item prices.py price1 price2 price3")
    sys.exit()
    
    prices = float(sys.argv[1]), float(sys.argv[2]), float(sys.argv[3])
    
    minimum_price = min(prices)
    maximum_price = max(prices)     
    average_price = sum(prices) / len(prices)
    
    #display results
    print("minimun prices:",minimum_price)
    print("maximum prices:",maximum_price)
    print("average prices:",average_price)
    
