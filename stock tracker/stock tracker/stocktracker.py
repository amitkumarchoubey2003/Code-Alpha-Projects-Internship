import yfinance as yf

portfolio = {}

def add_stock(symbol, shares):
    symbol = symbol.upper()
    portfolio[symbol] = portfolio.get(symbol, 0) + shares
    print(f"Added {shares} shares of {symbol}")

def remove_stock(symbol):
    symbol = symbol.upper()
    if symbol in portfolio:
        del portfolio[symbol]
        print(f"Removed {symbol} from portfolio")
    else:
        print("Stock not found in portfolio")

def track_portfolio():
    print("\nPortfolio Summary:")
    print(f"{'Symbol':<10} {'Shares':<10} {'Price':<10} {'Total Value':<15}")
    print("-" * 50)
    total_value = 0
    for symbol, shares in portfolio.items():
        stock = yf.Ticker(symbol)
        data = stock.history(period="1d")
        if not data.empty:
            price = data['Close'].iloc[0]  # Fixes the warning
            value = price * shares
            total_value += value
            print(f"{symbol:<10} {shares:<10} {price:<10.2f} {value:<15.2f}")
        else:
            print(f"{symbol:<10} {shares:<10} {'N/A':<10} {'N/A':<15}")
    print("-" * 50)
    print(f"{'Total Portfolio Value:':<32} ₹{total_value:.2f}")

# === Example usage ===
add_stock("AAPL", 10)
add_stock("TCS.NS", 3)
track_portfolio()
