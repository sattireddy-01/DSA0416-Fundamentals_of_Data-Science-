import numpy as np

# Sample recovery times (in days)
recovery_times = [3, 5, 7, 8, 9, 10, 12, 14, 16, 18, 20, 22, 25]

# Calculate percentiles using NumPy
percentiles = np.percentile(recovery_times, [10, 50, 90])

# Print results
print(f"10th Percentile: {percentiles[0]} days")
print(f"50th Percentile (Median): {percentiles[1]} days")
print(f"90th Percentile: {percentiles[2]} days")
