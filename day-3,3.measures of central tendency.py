import pandas as pd

purchase_data = [50, 30, 50, 40, 60, 70, 40, 50, 30, 50, 60]

purchase_series = pd.Series(purchase_data)
mean_purchase_amount = purchase_series.mean()
mode_purchase_amount = purchase_series.mode()[0]  

print(f"Mean (Average) Purchase Amount: ${mean_purchase_amount:.2f}")
print(f"Mode (Most Frequently Occurring) Purchase Amount: ${mode_purchase_amount}")
