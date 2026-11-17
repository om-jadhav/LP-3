# 0-1 Knapsack

# Number of items
n = 4

# Weights and values
weights = [2,3 , 4, 5]
values = [9, 4, 5, 6]

# Knapsack capacity
capacity = 5


# Function to find maximum profit
def knapsack(i, current_weight, current_value, selected):

    # All items are checked
    if i == n:
        return current_value, selected

    # Do not include current item
    profit1, items1 = knapsack(
        i + 1,
        current_weight,
        current_value,
        selected
    )

    # Include current item if it fits
    if current_weight + weights[i] <= capacity:
        profit2, items2 = knapsack(
            i + 1,
            current_weight + weights[i],
            current_value + values[i],
            selected + [i + 1]
        )
    else:
        profit2 = 0
        items2 = []

    # Choose the better option
    if profit2 > profit1:
        return profit2, items2
    else:
        return profit1, items1


# Find maximum profit and selected items
maximum_profit, selected_items = knapsack(0, 0, 0, [])

# Display result
print("Maximum profit:", maximum_profit)
print("Items included:", selected_items)