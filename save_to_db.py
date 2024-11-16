import psycopg2
from psycopg2 import OperationalError

class ConnectDatabase:
    def __init__(self):
        self.db = None
        self.cur = None

    def connectDB(self):
        self.db = psycopg2.connect(
            host="localhost",         
            user="postgres",          
            password="", 
            database="TickPrices",
            port=5432 
        )
        cur = self.db.cursor()
         
        table_sql = (f"""CREATE TABLE IF NOT EXISTS public.tick_prices (
            id SERIAL PRIMARY KEY,
            name VARCHAR(10) NOT NULL,
            exchange VARCHAR(10),
            quoteType INT,
            price DECIMAL(10,4),
            timestamp TIMESTAMP,
            marketHours INT,
            changePercent DECIMAL(10,4),
            day_volume INT,
            change DECIMAL(10, 4),
            price_hint INT,
            created_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
         )""")
        cur.execute(table_sql)
        self.db.commit()
        print("connection successfully!")
        cur.close()

    def execute_tick(self,msg):
        cur = self.db.cursor()

        sql = """
        INSERT INTO tick_prices (
            name, exchange, quoteType, price, timestamp, marketHours,
            changePercent, day_volume, change, price_hint
        ) VALUES (%s, %s, %s, %s, to_timestamp(%s / 1000), %s, %s, %s, %s, %s)
        """
        values = (
            msg['id'], msg['exchange'], msg['quoteType'], msg['price'], 
            msg['timestamp'], msg['marketHours'], msg['changePercent'],
            msg['dayVolume'], msg['change'], msg['priceHint']
        )
        cur.execute(sql, values)
        self.db.commit()
        print("insert data successfully!")
        cur.close()
