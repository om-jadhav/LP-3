# Fractional Knapsack using Greedy Method

# Items: (weight, profit)
items = [(10, 60), (20, 100), (30, 120)]

capacity = 50
total_profit = 0

# Calculate profit/weight ratio
items.sort(key=lambda item: item[1] / item[0], reverse=True)

for weight, profit in items:

    if capacity >= weight:
        # Take the complete item
        capacity -= weight
        total_profit += profit

    else:
        # Take the required fraction of the item
        fraction = capacity / weight
        total_profit += profit * fraction
        capacity = 0
        break

print("Maximum Profit =", total_profit)