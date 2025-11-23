import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def generate_synthetic_data(num_hours=720):
    """Generate synthetic hourly PM2.5 data with daily seasonality and noise."""
    date_rng = pd.date_range(start='2023-01-01', periods=num_hours, freq='H')
    daily_pattern = 20 + 10 * np.sin(np.linspace(0, 5 * np.pi, num_hours))
    noise = np.random.normal(0, 5, num_hours)
    pm25_values = daily_pattern + noise
    pm25_values = np.clip(pm25_values, 0, None)
    df = pd.DataFrame({'Date': date_rng, 'PM2.5': pm25_values})
    return df

def print_statistics(df):
    print("Data statistics:")
    print(df['PM2.5'].describe())

def rolling_average_predict(series, window=24):
    """Rolling average prediction with previous window values."""
    return series.rolling(window=window).mean().shift(1)

def train_test_split(df, train_ratio=0.8):
    split_idx = int(len(df) * train_ratio)
    return df.iloc[:split_idx], df.iloc[split_idx:]

def calculate_errors(actual, predicted):
    mae = np.mean(np.abs(actual - predicted))
    rmse = np.sqrt(np.mean((actual - predicted) ** 2))
    print(f"Mean Absolute Error (MAE): {mae:.3f}")
    print(f"Root Mean Squared Error (RMSE): {rmse:.3f}")

def plot_results(dates, actual, predicted):
    plt.figure(figsize=(14,6))
    plt.plot(dates, actual, label='Actual PM2.5')
    plt.plot(dates, predicted, label='Predicted PM2.5 (Rolling Avg)', linestyle='--')
    plt.xlabel('Date')
    plt.ylabel('PM2.5 Concentration')
    plt.title('Air Quality Prediction Example')
    plt.legend()
    plt.grid(True)
    plt.show()

def save_predictions(df, filename='pm25_predictions.csv'):
    df.to_csv(filename, index=False)
    print(f"Predictions saved to {filename}")

def main():
    df = generate_synthetic_data()
    print_statistics(df)

    train, test = train_test_split(df)
    
    train['Predicted_PM25'] = rolling_average_predict(train['PM2.5'])
    test['Predicted_PM25'] = rolling_average_predict(test['PM2.5'])

    # Remove NaNs from predictions for evaluation
    valid_test = test.dropna(subset=['Predicted_PM25'])
    
    calculate_errors(valid_test['PM2.5'], valid_test['Predicted_PM25'])
    plot_results(valid_test['Date'], valid_test['PM2.5'], valid_test['Predicted_PM25'])
    
    save_predictions(valid_test[['Date', 'PM2.5', 'Predicted_PM25']])

if __name__ == "__main__":
    main()
