def knapsack(capacity, weights, values):
    # dp[w] will store the max value possible for weight 'w'
    dp = [0] * (capacity + 1)

    # Loop through each item
    for i in range(len(weights)):
        weight = weights[i]
        value = values[i]

        # Loop backwards from capacity down to the item's weight
        for w in range(capacity, weight - 1, -1):
            dp[w] = max(dp[w], value + dp[w - weight])

    return dp[capacity]


# --- Example Usage ---
values = [60, 100, 120]
weights = [10, 20, 30]
capacity = 50

max_val = knapsack(capacity, weights, values)
print("Maximum value:", max_val)  # Output: 220

# # Fractional Knapsack using Greedy Method

# # Items: (weight, profit)
# items = [(10, 60), (20, 100), (30, 120)]

# capacity = 50
# total_profit = 0

# # Calculate profit/weight ratio
# items.sort(key=lambda item: item[1] / item[0], reverse=True)

# for weight, profit in items:

#     if capacity >= weight:
#         # Take the complete item
#         capacity -= weight
#         total_profit += profit

#     else:
#         # Take the required fraction of the item
#         fraction = capacity / weight
#         total_profit += profit * fraction
#         capacity = 0
#         break

# print("Maximum Profit =", total_profit)

def fractional_knapsack(capacity,values,weights):
    items = []

    for i in range(len(values)):
        ratio = values[i] / weights[i]
        items.append([ratio,values[i],weights[i]])

    items.sort(reverse = True)

    total_value = 0.0

    for item in items:
        ratio = item[0]
        value = item[1]
        weight = item[2]

        if capacity >= weight:
            capacity = capacity - weight
            total_value += value

        else:
            fraction = capacity / weight
            total_value += fraction * value
            break

    return total_value

# Driver code
values = [60, 100, 120]
weights = [10, 20, 30]
capacity = 50

max_value = fractional_knapsack(capacity, values, weights)
print("Maximum value in Knapsack =", max_value)

N = 8

def is_safe(board, row, col):
    for r in range(row):
        # Find which column has the queen in row 'r'
        c = board[r].index(1)
        
        # Check same column OR same diagonal
        if c == col or abs(r - row) == abs(c - col):
            return False
    return True

def solve(board, row=1):
    if row == N:
        for r in board:
            print(" ".join("Q" if x else "." for x in r))
        return True

    for col in range(N):
        if is_safe(board, row, col):
            board[row][col] = 1
            if solve(board, row + 1):
                return True
            board[row][col] = 0  # Backtrack

    return False

board = [[0] * N for _ in range(N)]
board[0][0] = 1
solve(board)

# 1. Import libraries
import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.metrics import accuracy_score, confusion_matrix

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

# 2. Load dataset
df = pd.read_csv("Churn_Modelling.csv")

print(df.head())
print(df.isnull().sum())

# 3. Drop unnecessary columns
df = df.drop(['RowNumber', 'CustomerId', 'Surname'], axis=1)

# 4. Encode categorical columns
le = LabelEncoder()

df['Gender'] = le.fit_transform(df['Gender'])
df['Geography'] = le.fit_transform(df['Geography'])

# 5. Separate input and output
X = df.drop('Exited', axis=1)
y = df['Exited']

# 6. Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# 7. Normalize data
scaler = StandardScaler()

X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# 8. Build neural network
model = Sequential()

model.add(Dense(64, activation='relu', input_shape=(X_train.shape[1],)))
model.add(Dense(32, activation='relu'))
model.add(Dense(1, activation='sigmoid'))

# 9. Compile model
model.compile(
    optimizer='adam',
    loss='binary_crossentropy',
    metrics=['accuracy']
)

# 10. Train model
model.fit(X_train, y_train, epochs=25, batch_size=32)

# 11. Predict
y_pred = (model.predict(X_test) > 0.5).astype(int)

# 12. Evaluate
print("Accuracy:", accuracy_score(y_test, y_pred))
print("Confusion Matrix:")
print(confusion_matrix(y_test, y_pred))

