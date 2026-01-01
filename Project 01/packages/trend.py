import pandas as pd, numpy as np,matplotlib.pyplot as plt, seaborn as sns 


def trend_analysis(data):
    print("Trend Analysis using Moving Average")

    try:
        date_col = input("Enter date column name (e.g., date): ")
        price_col = input("Enter price column name (open or close): ")
        window = int(input("Enter moving average window (e.g., 20): "))

        if date_col not in data.columns:
            raise ValueError(f"{date_col} column not found")
        if price_col not in data.columns:
            raise ValueError(f"{price_col} column not found")
        data[date_col] = pd.to_datetime(data[date_col])
        data = data.sort_values(date_col)
        data['SMA'] = data[price_col].rolling(window=window).mean()
        plt.figure(figsize=(12, 6))
        plt.plot(data[date_col], data[price_col], label=price_col)
        plt.plot(data[date_col], data['SMA'], label=f'{window}-Day SMA')

        plt.title("Trend Analysis")
        plt.xlabel("Date")
        plt.ylabel("Price")
        plt.legend()
        plt.grid(True)
        plt.show()

        latest_price = data[price_col].iloc[-1]
        latest_sma = data['SMA'].iloc[-1]

        print("\nTrend Summary:")
        print(f"Latest Price : {latest_price:.2f}")
        print(f"Latest SMA   : {latest_sma:.2f}")

        if latest_price > latest_sma:
            print("Market Trend: UPTREND")
        elif latest_price < latest_sma:
            print("Market Trend: DOWNTREND")
        else:
            print("Market Trend: SIDEWAYS")
    except Exception as e:
        print("Error:", e)
        
        
        
def daily_returns_calculation(data):
    print("Calculating Daily Returns...")
    try:
        column = input("Enter the column name for daily returns calculation (e.g., 'Close'): ")
        
        data['Daily Return'] = data[column].pct_change() * 100
        
        plt.figure(figsize=(12,6))
        plt.plot(data['Daily Return'], label='Daily Return', color="#FF5733")
        plt.title('Daily Returns Over Time')
        plt.xlabel('Date')
        plt.ylabel('Daily Return (%)')
        plt.legend()
        plt.show()
        
        latest_return = data['Daily Return'].iloc[-1]
        avg_return = data['Daily Return'].mean()
        max_return = data['Daily Return'].max()
        min_return = data['Daily Return'].min()

        print("\nDaily Returns Summary:")
        print(f"Latest Daily Return : {latest_return:.2f}%")
        print(f"Average Return      : {avg_return:.2f}%")
        print(f"Highest Return      : {max_return:.2f}%")
        print(f"Lowest Return       : {min_return:.2f}%")

        if latest_return > 0:
            print("Price increased compared to previous day")
        elif latest_return < 0:
            print("Price decreased compared to previous day")
        else:
            print("No price change from previous day")
    except Exception as e:
        print(f"An error occurred during daily returns calculation: {e}")
    
    
        
def moving_average_analysis(data):
    print("Performing Moving Average Analysis...")
    try:
        column = input("Enter the column name for moving average analysis (e.g., 'Close'): ")
        short_window = int(input("Enter the short moving average window size (e.g., 20): "))
        long_window = int(input("Enter the long moving average window size (e.g., 50): "))
        
        data['Short_MA'] = data[column].rolling(window=short_window).mean()
        data['Long_MA'] = data[column].rolling(window=long_window).mean()
        
        plt.figure(figsize=(12,6))
        plt.plot(data[column], label=f'{column} Price', color="#061E29")
        plt.plot(data['Short_MA'], label=f'{short_window}-Day MA', color='#5F9598')
        plt.plot(data['Long_MA'], label=f'{long_window}-Day MA', color='#FF5733')
        plt.title('Moving Average Analysis')
        plt.xlabel('Date')
        plt.ylabel('Price')
        plt.legend()
        plt.show()
        
        latest_price = data[column].iloc[-1]
        short_ma = data['Short_MA'].iloc[-1]
        long_ma = data['Long_MA'].iloc[-1]

        print("\nMoving Average Summary:")
        print(f"Latest Price : {latest_price:.2f}")
        print(f"Short MA     : {short_ma:.2f}")
        print(f"Long MA      : {long_ma:.2f}")

        if short_ma > long_ma:
            print("Trend Signal: UPTREND (Bullish)")
        elif short_ma < long_ma:
            print("Trend Signal: DOWNTREND (Bearish)")
        else:
            print("Trend Signal: SIDEWAYS")
        
    except Exception as e:
        print(f"An error occurred during moving average analysis: {e}")
            
def volatility_analysis(data):
    print("Performing Volatility Analysis...")
    try:
        column = input("Enter the column name for volatility analysis (e.g., 'Close'): ")
        window_size = int(input("Enter the rolling window size for volatility calculation (e.g., 20): "))
        
        data['Log_Returns'] = np.log(data[column] / data[column].shift(1))
        data['Volatility'] = data['Log_Returns'].rolling(window=window_size).std() * np.sqrt(window_size)
        
        plt.figure(figsize=(12,6))
        plt.plot(data['Volatility'], label='Volatility', color="#4B84FF")
        plt.title('Volatility Over Time')
        plt.xlabel('Date')
        plt.ylabel('Volatility')
        plt.legend()
        plt.show()
        
        latest_volatility = data['Volatility'].iloc[-1]
        avg_volatility = data['Volatility'].mean()
        max_volatility = data['Volatility'].max()
        min_volatility = data['Volatility'].min()

        print("\nVolatility Summary:")
        print(f"Latest Volatility : {latest_volatility:.4f}")
        print(f"Average Volatility: {avg_volatility:.4f}")
        print(f"Highest Volatility: {max_volatility:.4f}")
        print(f"Lowest Volatility : {min_volatility:.4f}")

        if latest_volatility > avg_volatility:
            print("Market Condition: HIGH VOLATILITY (Risky)")
        else:
            print("Market Condition: LOW / NORMAL VOLATILITY (Stable)")
        
    except Exception as e:
        print(f"An error occurred during volatility analysis: {e}")
