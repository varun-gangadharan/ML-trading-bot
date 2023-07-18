import pandas as pd
import numpy as np
from sklearn.svm import SVR
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split

# Read data
data = pd.read_csv('data.csv', parse_dates=['Date'], index_col='Date')

# Create lagged features
data['Open_lag1'] = data['Open'].shift(1)
data['High_lag1'] = data['High'].shift(1)
data['Low_lag1'] = data['Low'].shift(1)
data['Close_lag1'] = data['Close'].shift(1)
data['Volume_lag1'] = data['Volume'].shift(1)

# Drop the rows with missing values
data.dropna(inplace=True)

# Define features and target
features = ['Open_lag1', 'High_lag1', 'Low_lag1', 'Close_lag1', 'Volume_lag1']
target = 'Close'

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(
    data[features],
    data[target],
    test_size=0.2,
    shuffle=False # Important for time series data
)

# Standardize features
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Train the model
model = SVR(kernel='rbf', C=100, gamma=0.1, epsilon=.1)
model.fit(X_train, y_train)

# Make predictions
y_train_pred = model.predict(X_train)
y_test_pred = model.predict(X_test)

# Calculate errors
train_error = y_train - y_train_pred
test_error = y_test - y_test_pred

# Generate trading signals
# Buy if the error is positive (predicted price is lower than the actual)
# Sell if the error is negative (predicted price is higher than the actual)
train_signal = np.where(train_error > 0, 'Buy', 'Sell')
test_signal = np.where(test_error > 0, 'Buy', 'Sell')
