import yfinance as yf
import pandas as pd

try:
    data = yf.download('MSFT', start='2024-01-01', end='2024-07-01', timeout=30)

    if data.empty:
        print("❌ No data fetched. Please check your internet or ticker.")
    else:
        data['Signal'] = (data['Close'] > data['Open']).astype(int)
        data.to_csv('signals.csv')
        print("✅ Signal file created with trading signals.")
except Exception as e:
    print("⚠️ Error while downloading stock data:", e)

