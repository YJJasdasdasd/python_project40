# 가상화폐 종류를 알기위해 사용하는 pyupbit import
import datetime
import pandas as pd
from datetime import datetime
import sqlite3
import pyupbit

# 가상화폐 종류를 추출
coin_lists = pyupbit.get_tickers(fiat="KRW")

price_now = pyupbit.get_current_price(["KRW-BTC", "KRW-ETH"])
print(price_now)


# 비트코인 데이터를 한화로 불러옴
ticker = "KRW-BTC"
# 분단위 데이터
interval = 'minute1'
# 현제 날짜와 시간
to = datetime.now()
# 200개의 데이터
count = 200
# 현제 날짜, 시간의 비트코인 분단위 데이터 200개를 데이터 프레임 형식으로 불러옴
price_now = pyupbit.get_ohlcv(
    ticker=ticker, interval=interval, to=to, count=count)

# 저장 경로와 파일 이름 설정
db_path = r"C:\Users\user\python\coin.db"

# 데이터 베이스 생성
con = sqlite3.connect(db_path, isolation_level=None)
# BTC이름으로 데이터를 생성후 데이터 추가
price_now.to_sql('BTC', con, if_exists='append')
# 데이터 베이스 닫기
con.close

#  sqlite3.connect에서 isolation_level = None 옵셩을 작성하면
#  db에서 update, insert, delete를 할 경우 자동 커밋


db_path = r"C:\Users\user\python\coin.db"
con = sqlite3.connect(db_path, isolation_level=None)

readed_df = pd.read_sql("SELECT * FROM 'BTC'", con, index_col='index')

print(readed_df)

readed_df['value']


def date_range(start, end):
    start = datetime.datetime.strptime(start, "%Y-%m-%d")
    start = start + datetime.timedelta(days=1)
    end = datetime. datetime.strptime(end, "%Y-%m-%d")
    end = end + datetime.timedelta(days=1)
    dates = [(start + datetime.timedelta(days=1)).strftime("%Y-%m-%d")
             for i in range((end-start).days+1)]
    return dates


dates = date_range("2022-11-01", "2022-11-02")

print(dates)

for day in reversed(dates):
    myDay = day + '00:00'
    print(myDay)

    ticker = 'KRW-BTC'
    interval = 'minute1'
    to = myDay
    count = 1440
    price_now = pyupbit.get_ohlcv(
        ticker=ticker, interval=interval, count=count)

    print(price_now)

    db_path = r"C:\Users\user\python\coin1.db"

    con = sqlite3.connect(db_path, isolation_level=None)
    price_now.to_sql("BTC", con, if_exists='append')

    con.close


db_path = r"C:\Users\user\python\coin1.db"
con = sqlite3.connect(db_path, isolation_level=None)

readed_df = pd.read_sql(
    "SELECT DISTINCT * FROM 'BTC_NEW'", con, index_col='index')

readed_df.to_sql("BTC_NEW", con, if_exists='replace')

print(readed_df)

readed_df
