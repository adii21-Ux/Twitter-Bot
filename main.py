from nsetools import Nse
import time
import stockFetch

def run():
    nse = Nse()
    stockList = ['INFY', 'HCLTECH', 'WIPRO']
    i=0
    size = len(stockList)
    
    while(1):
        stock = stockList[i%size]
        params = nse.get_quote(stock)
        keyValues = ["companyName", "dayHigh", "basePrice", "dayLow", "buyPrice1", "lastPrice"]
        
        values = []
        for key,value in params.items():
            if key in keyValues:
                values.append(key + ":" + str(value))
        
        stockFetch.tweet(values)
        
        i = i+1
        time.sleep(20)
        
    
if __name__ == '__main__':
    run()