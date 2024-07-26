from scipy import stats

# Example purchase amounts data
purchase_amounts = [20, 30, 40, 50, 30, 40, 50, 60, 70, 80, 90, 100, 100, 100]

# Calculate the mean (average) purchase amount
mean_purchase_amount = sum(purchase_amounts) / len(purchase_amounts)

# Calculate the mode of the purchase amounts
mode_purchase_amount = stats.mode(purchase_amounts)

# Output the results
print("Mean purchase amount:", mean_purchase_amount, "dollars")
print("Mode of purchase amounts:", mode_purchase_amount.mode, "dollars")
