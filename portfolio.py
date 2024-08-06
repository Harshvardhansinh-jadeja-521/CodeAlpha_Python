import requests
import pandas as pd

ALPHA_VANTAGE_API_KEY = 'TIBNM2TSAU42IZ4N'

class Portfolio:
    def __init__(self):
        self.stocks = {}

    def add_stock(self, symbol, quantity, purchase_price):
        if symbol in self.stocks:
            self.stocks[symbol]['quantity'] += quantity
            self.stocks[symbol]['purchase_price'] = purchase_price
        else:
            self.stocks[symbol] = {'quantity': quantity, 'purchase_price': purchase_price}

    def remove_stock(self, symbol, quantity):
        if symbol in self.stocks:
            self.stocks[symbol]['quantity'] -= quantity
            if self.stocks[symbol]['quantity'] <= 0:
                del self.stocks[symbol]
        else:
            print(f"Stock {symbol} not found in portfolio.")

    def get_stock_data(self, symbol):
        url = f'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol={symbol}&interval=1min&apikey={ALPHA_VANTAGE_API_KEY}'
        response = requests.get(url)
        data = response.json()
        try:
            time_series = data['Time Series (1min)']
            latest_time = sorted(time_series.keys())[0]
            latest_data = time_series[latest_time]
            return {
                'price': float(latest_data['1. open']),
                'high': float(latest_data['2. high']),
                'low': float(latest_data['3. low']),
                'volume': int(latest_data['5. volume'])
            }
        except KeyError:
            print("Error fetching data for symbol:", symbol)
            return None

    def display_portfolio(self):
        portfolio_data = []
        for symbol, details in self.stocks.items():
            stock_data = self.get_stock_data(symbol)
            if stock_data:
                current_price = stock_data['price']
                market_value = current_price * details['quantity']
                profit_loss = market_value - (details['purchase_price'] * details['quantity'])
                portfolio_data.append({
                    'Symbol': symbol,
                    'Quantity': details['quantity'],
                    'Purchase Price': details['purchase_price'],
                    'Current Price': current_price,
                    'Market Value': market_value,
                    'Profit/Loss': profit_loss
                })
        df = pd.DataFrame(portfolio_data)
        print(df)

if __name__ == "__main__":
    portfolio = Portfolio()
    while True:
        print("\nStock Portfolio Tracker")
        print("1. Add Stock")
        print("2. Remove Stock")
        print("3. Display Portfolio")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            symbol = input("Enter stock symbol: ").upper()
            quantity = int(input("Enter quantity: "))
            purchase_price = float(input("Enter purchase price: "))
            portfolio.add_stock(symbol, quantity, purchase_price)
        elif choice == '2':
            symbol = input("Enter stock symbol: ").upper()
            quantity = int(input("Enter quantity to remove: "))
            portfolio.remove_stock(symbol, quantity)
        elif choice == '3':
            portfolio.display_portfolio()
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please try again.")