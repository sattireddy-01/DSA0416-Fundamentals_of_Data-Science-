import numpy as np

# Example recovery times data (in days)
recovery_times = [3, 5, 7, 9, 11, 13, 15, 17, 19, 21]

# Calculating percentiles
percentiles = np.percentile(recovery_times, [10, 50, 90])

# Outputting results
print("10th percentile:", percentiles[0], "days")
print("50th percentile (median):", percentiles[1], "days")
print("90th percentile:", percentiles[2], "days")
