# Air Quality Prediction and Visualization

## Project Overview

This project simulates hourly air quality data (PM2.5 concentrations) and performs a basic prediction using a rolling average method. It visualizes actual PM2.5 levels versus predicted values and computes error metrics to evaluate prediction performance. The solution is designed as a modular Python project.

## Features

- Synthetic data generation mimicking real-world air pollution patterns
- Data split into training and testing subsets
- Rolling average predictions to estimate future PM2.5 values
- Error metrics calculation: Mean Absolute Error (MAE) and Root Mean Squared Error (RMSE)
- Visualization of actual and predicted pollutant levels over time
- Saving predictions to CSV for further analysis

## Project Structure

- `air_quality_utils.py`: Contains utility functions for data generation, prediction, evaluation, plotting, and file saving.
- `air_quality_model.py`: Main script coordinating the workflow by calling utilities and managing data split, prediction, and output.

## Setup Instructions

### Prerequisites

- Python 3.7 or newer
- Python packages: pandas, numpy, matplotlib

### Installation of Dependencies

Run this command to install required libraries if not already installed:


## Running the Project

1. Ensure both `air_quality_utils.py` and `air_quality_model.py` are in the same directory.
2. Execute the main script:


3. The script will:
    - Generate synthetic air quality data (720 hours).
    - Print descriptive statistics.
    - Split data into train and test sets (80/20 split).
    - Compute rolling average predictions on both subsets.
    - Calculate and print MAE and RMSE on test data.
    - Visualize actual vs predicted PM2.5 values.
    - Save predictions to `pm25_predictions.csv`.

## Code Summary

### air_quality_utils.py (Key functions)

- `generate_synthetic_data(num_hours=720)`: Creates synthetic hourly PM2.5 data simulating daily cycles and random noise.
- `print_statistics(df)`: Prints summary statistics of the dataset.
- `rolling_average_predict(series, window=24)`: Computes rolling average prediction shifted by one time step.
- `train_test_split(df, train_ratio=0.8)`: Splits DataFrame into training and testing portions.
- `calculate_errors(actual, predicted)`: Computes MAE and RMSE between actual and predicted values.
- `plot_results(dates, actual, predicted)`: Plots time series line chart for actual and predicted values.
- `save_predictions(df, filename)`: Saves DataFrame with Date, actual and predicted PM2.5 to CSV.

### air_quality_model.py (Workflow)

- Uses all utilities to implement the project flow:
  - Data generation and statistics printing
  - Data splitting into train/test
  - Performing predictions
  - Error calculation and reporting
  - Visualization
  - Exporting prediction results

## Customization Tips

- Adjust `num_hours` in `generate_synthetic_data()` to simulate longer or shorter datasets.
- Modify rolling window size in `rolling_average_predict()` to smooth predictions differently.
- Replace rolling average with machine learning or deep learning models for better accuracy.
- Integrate real air quality datasets by modifying data loading logic.

---

Feel free to contribute or report issues for further improvements!
