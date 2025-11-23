from air_quality_utils import (
    generate_synthetic_data, print_statistics,
    rolling_average_predict, train_test_split,
    calculate_errors, plot_results, save_predictions
)

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
