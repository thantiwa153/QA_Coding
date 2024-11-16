from ticker_price import *
from save_to_db import *

def main():
   
    print(f"running main method ")
    db = ConnectDatabase()
    db.connectDB()
    ticker_data = tickerPrices(db)
    ticker_data.run()
    print("done")
   
if __name__ == "__main__":
    main()