import numpy as np
import scipy.stats as stats

# Sample data (conversion rates)
np.random.seed(42)

# Sample sizes
n_A = 10 # number of visitors for design A
n_B = 10 # number of visitors for design B

# Conversion rates (simulated or actual data)
conversion_rate_A = [2,4,7,6,5,4,9,0,8,2]
conversion_rate_B = [3,6,8,7,9,2,1,9,0,5]

# Calculate sample statistics
mean_A = np.mean(conversion_rate_A)
mean_B = np.mean(conversion_rate_B)
std_A = np.std(conversion_rate_A, ddof=1)  # unbiased standard deviation
std_B = np.std(conversion_rate_B, ddof=1)  # unbiased standard deviation

# Perform independent t-test
t_statistic, p_value = stats.ttest_ind(conversion_rate_A, conversion_rate_B)

# Print results
print(f"Mean conversion rate for design A: {mean_A:.4f}")
print(f"Mean conversion rate for design B: {mean_B:.4f}")
print(f"Standard deviation for design A: {std_A:.4f}")
print(f"Standard deviation for design B: {std_B:.4f}")
print(f"T-statistic: {t_statistic:.4f}")
print(f"P-value: {p_value:.4f}")

# Compare p-value with significance level (α = 0.05)
alpha = 0.05
if p_value < alpha:
    print("There is a statistically significant difference in the mean conversion rates between designs A and B.")
else:
    print("There is no statistically significant difference in the mean conversion rates between designs A and B.")
