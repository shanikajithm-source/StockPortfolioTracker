
import csv
import math
from datetime import datetime
import yfinance as yf

print("================================")
print("     STOCK PORTFOLIO TRACKER")
print("================================")

portfolio = {}

# Ask how many stocks
while True:
    try:
        n = int(input("How many stocks do you want to add? "))
        if n > 0:
            break
        print("Enter a number greater than zero.")
    except ValueError:
        print("Please enter a valid whole number.")

# Collect stock details
for i in range(n):

    print("\nEnter details for Stock", i + 1)

    while True:
        ticker = input("Enter stock symbol: ").strip().upper()

        if not ticker:
            print("Ticker cannot be empty.")
            continue

        if ticker in portfolio:
            print("This stock is already added.")
            continue

        print("Fetching latest available price...")

        try:
            stock = yf.Ticker(ticker)
            data = stock.history(period="5d")

            if data.empty:
                print("No price data found. Try another ticker.")
                continue

            current_price = float(data["Close"].iloc[-1])

            if not math.isfinite(current_price) or current_price <= 0:
                print("Invalid market price. Try another ticker.")
                continue

            price_date = str(data.index[-1].date())

            print("Latest closing price: $", round(current_price, 2))
            print("Price date:", price_date)
            break

        except Exception as error:
            print("Unable to fetch price:", error)
            print("Check your internet connection and try again.")

    # Validate buying price
    while True:
        try:
            buy_price = float(input("Enter buying price: "))

            if math.isfinite(buy_price) and buy_price > 0:
                break

            print("Buying price must be positive.")

        except ValueError:
            print("Enter a valid number.")

    # Validate quantity
    while True:
        try:
            quantity = int(input("Enter number of shares: "))

            if quantity > 0:
                break

            print("Quantity must be greater than zero.")

        except ValueError:
            print("Enter a valid whole number.")

    # Store stock details
    portfolio[ticker] = {
        "buy_price": buy_price,
        "quantity": quantity,
        "current_price": current_price,
        "price_date": price_date
    }

total_investment = 0
total_market_value = 0

timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

print("\n================================")
print("       PORTFOLIO SUMMARY")
print("================================")

with open("portfolio_summary.csv", "a", newline="", encoding="utf-8") as file:

    writer = csv.writer(file)

    writer.writerow([])
    writer.writerow(["Portfolio Report", timestamp])

    writer.writerow([
        "Stock",
        "Quantity",
        "Buying Price",
        "Current Price",
        "Price Date",
        "Investment",
        "Market Value",
        "Profit/Loss",
        "Return Percentage"
    ])

    for ticker, details in portfolio.items():

        buy_price = details["buy_price"]
        quantity = details["quantity"]
        current_price = details["current_price"]

        investment = buy_price * quantity
        market_value = current_price * quantity

        profit_loss = market_value - investment
        percentage = (profit_loss / investment) * 100

        total_investment += investment
        total_market_value += market_value

        print("\nStock:", ticker)
        print("Buying Price: $", round(buy_price, 2))
        print("Current Price: $", round(current_price, 2))
        print("Quantity:", quantity)
        print("Price Date:", details["price_date"])
        print("Investment: $", round(investment, 2))
        print("Market Value: $", round(market_value, 2))
        print("Profit/Loss: $", round(profit_loss, 2))
        print("Return:", round(percentage, 2), "%")

        if profit_loss > 0:
            print("Status: PROFIT")
        elif profit_loss < 0:
            print("Status: LOSS")
        else:
            print("Status: NO PROFIT NO LOSS")

        print("--------------------------------")

        writer.writerow([
            ticker,
            quantity,
            round(buy_price, 2),
            round(current_price, 2),
            details["price_date"],
            round(investment, 2),
            round(market_value, 2),
            round(profit_loss, 2),
            round(percentage, 2)
        ])

    total_profit = total_market_value - total_investment
    total_percentage = (total_profit / total_investment) * 100

    print("\n========== TOTAL PORTFOLIO ==========")
    print("Total Investment: $", round(total_investment, 2))
    print("Total Market Value: $", round(total_market_value, 2))
    print("Total Profit/Loss: $", round(total_profit, 2))
    print("Overall Return:", round(total_percentage, 2), "%")
    print("=====================================")

    writer.writerow([
        "TOTAL", "", "", "", "",
        round(total_investment, 2),
        round(total_market_value, 2),
        round(total_profit, 2),
        round(total_percentage, 2)
    ])

print("\nPortfolio summary saved successfully!")
print("File name: portfolio_summary.csv")
print("Note: Market prices are latest available closing prices.")
