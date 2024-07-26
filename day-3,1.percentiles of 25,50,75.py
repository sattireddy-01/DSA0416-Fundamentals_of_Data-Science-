import numpy as np

# Sample response times (in milliseconds)
response_times = [120, 150, 180, 200, 210, 230, 250, 280, 300, 320]

# Calculate percentiles using NumPy
percentiles = np.percentile(response_times, [25, 50, 75])

# Print results
print(f"25th Percentile (Q1): {percentiles[0]} ms")
print(f"50th Percentile (Median): {percentiles[1]} ms")
print(f"75th Percentile (Q3): {percentiles[2]} ms")
