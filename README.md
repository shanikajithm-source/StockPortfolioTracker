# Stock Portfolio Performance Tracker

## Project Overview

Stock Portfolio Performance Tracker is a Python-based command-line application that helps users monitor stock investments and calculate portfolio performance.

The application retrieves the latest available closing prices using Yahoo Finance through the `yfinance` library and generates a CSV report.

## Features

- Add multiple stocks using ticker symbols.
- Enter purchase prices and share quantities.
- Automatically retrieve the latest available closing prices.
- Calculate invested capital and current market value.
- Calculate individual stock profit/loss and return percentage.
- Calculate total portfolio performance.
- Validate user inputs and handle unavailable stock-price data.
- Save portfolio reports with timestamps to a CSV file.

## Technologies Used

- Python
- yfinance
- CSV module
- datetime module
- Visual Studio Code

## Installation

**1. Clone the repository**

```bash
git clone https://github.com/YOUR-USERNAME/StockPortfolioTracker.git
cd StockPortfolioTracker
```

**2. Install dependencies**

```bash
python -m pip install -r requirements.txt
```

**3. Run the application**

```bash
python portfolio.py
```

## Sample Portfolio Results

The following results are based on example purchase prices and closing prices retrieved for October 23, 2026.

| Stock | Investment | Market Value | Profit/Loss | Return |
|---|---:|---:|---:|---:|
| AAPL | $1,500.00 | $3,477.30 | +$1,977.30 | +131.82% |
| MSFT | $1,500.00 | $2,622.55 | +$1,122.55 | +74.84% |
| **TOTAL** | **$3,000.00** | **$6,099.85** | **+$3,099.85** | **+103.33%** |

## Output

The program generates a file named `portfolio_summary.csv` containing stock information, price dates, invested amounts, market values, profits/losses, and return percentages.

## Limitations

- An internet connection is required to retrieve market prices.
- Prices are the latest available closing prices, not guaranteed real-time quotes.
- Calculations exclude transaction fees, taxes, dividends, and currency conversion.
- Stock purchase prices and quantities are entered manually.
- Repeated runs append additional reports to the CSV file.

## Future Improvements

- Add historical portfolio performance charts.
- Create a graphical dashboard.
- Support different currencies.
- Store stock transactions in a database.
- Export reports to Excel.

## Project Type

Python Internship Assignment — Stock Portfolio Performance Tracker