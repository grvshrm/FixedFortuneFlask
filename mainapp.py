from flask import Flask, request
import yfinance as yf
from db_utils.db_connect import connect
from db_utils.queries import *

MEASURES = ['symbol', 'currentPrice', 'open', 'dayHigh', 'dayLow', 'previousClose']
conn = connect()

app = Flask(__name__)

@app.route('/')
@app.route('/index/')
def index():
    return {'message':'Home Page!'} 

@app.post('/setticker/')
def set_ticker():
    data = {}
    symbol = request.get_json()['ticker']
    info = yf.Ticker(symbol).info
    for measure in MEASURES:
        data[measure] = info[measure]
    with conn:
        with conn.cursor() as cursor:
            cursor.execute(CREATE_STOCKS_TABLE)
            cursor.execute(CREATE_PORTFOLIO_TABLE)
            cursor.execute(INSERT_STOCK_DATA, tuple(data.values()))
            cursor.execute(INSERT_STOCK_IN_PORTFOLIO, (symbol, round(data['currentPrice'] - data['previousClose'], 2)))
    return data, 200

@app.get('/getportfolio/')
def get_portfolio():
    data = {}
    with conn:
        with conn.cursor() as cursor:
            cursor.execute(GET_PORTFOLIO)
            portfolio = cursor.fetchall()
    for stock in portfolio:
        data[stock[0]] = stock[1]
    return data, 200

@app.get('/getdelta/')
def get_delta():
    data = {}
    with conn:
        with conn.cursor() as cursor:
            cursor.execute(GET_STOCKS_DATA)
            info = cursor.fetchall()
    for stock in info:
        data[stock[0]] = {
            'price': stock[1], 
            'close': stock[2], 
            'delta': stock[3]
        }
    return data, 200

@app.get('/getstockprice/<ticker>')
def get_stock_price(ticker:str):
    data = {}
    with conn:
        with conn.cursor() as cursor:
            cursor.execute(GET_STOCK_PRICE, (ticker,))
            price = cursor.fetchone()[0]
    data[ticker] = price
    return data, 200