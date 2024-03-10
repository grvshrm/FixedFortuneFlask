CREATE_STOCKS_TABLE = "CREATE TABLE IF NOT EXISTS stocks (symbol TEXT PRIMARY KEY, price REAL, open REAL, high REAL, low REAL, close REAL);"
CREATE_PORTFOLIO_TABLE = "CREATE TABLE IF NOT EXISTS portfolio (id SERIAL PRIMARY KEY , symbol TEXT, delta REAL, FOREIGN KEY(symbol) REFERENCES stocks(symbol) ON DELETE CASCADE);"

INSERT_STOCK_DATA = "INSERT INTO stocks VALUES (%s, %s, %s, %s, %s, %s);"
INSERT_STOCK_IN_PORTFOLIO = "INSERT INTO portfolio (symbol, delta) VALUES (%s, %s);"

GET_PORTFOLIO = "SELECT id, symbol FROM portfolio;"
GET_STOCKS_DATA = "SELECT stocks.symbol, stocks.price, stocks.close, portfolio.delta FROM stocks JOIN portfolio ON stocks.symbol = portfolio.symbol;"

GET_STOCK_PRICE = "SELECT price FROM STOCKS WHERE symbol = %s;"