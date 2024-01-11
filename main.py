from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import metrics
import pandas as pd
import numpy as np

first_name = input("Enter the first name: ")
last_name = input("Enter the last name: ")

first_name_lowercase = first_name.lower() 
last_name_lowercase = last_name.lower() 

# Take the first letter of the first name
last_initial = last_name_lowercase[0]


# Concatenate the strings in the required format
url = f"https://www.basketball-reference.com/players/{last_initial}/{last_name_lowercase[:5]}{first_name_lowercase[:2]}01.html#all_last5"

df = pd.read_html(url)[0]

# Select features and target
features = ['FGA', '3PA', 'FTA']
target = ['PTS']

X = df[features]
y = df[target]

# Split the data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create and train the model
model = LinearRegression()
model.fit(X_train, y_train)

# Make predictions
y_pred = model.predict(X_test)

# Display the prediction
print(f"Based on the last 5 games, {first_name} {last_name} will score approximately {y_pred[0][0]:.2f} points in the next game.\n")

# Evaluate the model
print('Mean Absolute Error:', metrics.mean_absolute_error(y_test, y_pred))
print('Mean Squared Error:', metrics.mean_squared_error(y_test, y_pred))
print('Root Mean Squared Error:', np.sqrt(metrics.mean_squared_error(y_test, y_pred)))
