import numpy as np

# Example response times
response_times = [10, 15, 20, 25, 30, 35, 40, 45, 50, 55]

# Calculating percentiles
percentiles = np.percentile(response_times, [25, 50, 75])

# Outputting results
print("25th percentile:", percentiles[0])
print("50th percentile (median):", percentiles[1])
print("75th percentile:", percentiles[2])
