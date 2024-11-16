import yliveticker
import logging
from save_to_db import *

class tickerPrices:
    def __init__(self,db):
        self.db = db

    def run(self):
        # Configure logging
        logging.basicConfig(level=logging.INFO)

        # This function is called on each ticker update
        def on_new_msg(ws, msg):
            try:
                logging.info(msg)
                self.db.execute_tick(msg)
            except Exception as e:
                logging.error(f"Error processing message: {e}")

        # Subscribe to a list of tickers to get real-time updates
        yliveticker.YLiveTicker(
            on_ticker=on_new_msg,
            ticker_names=[
                "CPALL.BK", "PTT.BK", "THB=X", "BTC=X", "^GSPC", "ES=F", "CL=F", "GC=F", "SI=F"
            ],
        )

