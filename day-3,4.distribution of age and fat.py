import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import scipy.stats as stats

# Sample data
data = {
    'age': [25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100, 105, 110],
    'body_fat_percent': [15.2, 18.5, 20.3, 22.1, 24.5, 26.7, 28.3, 30.5, 32.1, 34.2, 36.4, 38.1, 40.2, 42.5, 44.3, 46.2, 48.5, 50.2]
}

# Create DataFrame
df = pd.DataFrame(data)

# Calculate mean, median, and standard deviation
mean_age = df['age'].mean()
median_age = df['age'].median()
std_dev_age = df['age'].std()

mean_body_fat = df['body_fat_percent'].mean()
median_body_fat = df['body_fat_percent'].median()
std_dev_body_fat = df['body_fat_percent'].std()

print("Age:")
print(f"Mean: {mean_age}")
print(f"Median: {median_age}")
print(f"Standard Deviation: {std_dev_age}")

print("\nBody Fat Percentage:")
print(f"Mean: {mean_body_fat}")
print(f"Median: {median_body_fat}")
print(f"Standard Deviation: {std_dev_body_fat}")

# Draw boxplots
plt.figure(figsize=(10, 6))
plt.subplot(1, 2, 1)
sns.boxplot(y='age', data=df)
plt.title('Boxplot of Age')

plt.subplot(1, 2, 2)
sns.boxplot(y='body_fat_percent', data=df)
plt.title('Boxplot of Body Fat Percentage')

plt.tight_layout()
plt.show()

# Draw scatter plot
plt.figure(figsize=(8, 6))
plt.scatter(df['age'], df['body_fat_percent'])
plt.title('Scatter Plot of Age vs Body Fat Percentage')
plt.xlabel('Age')
plt.ylabel('Body Fat Percentage')
plt.grid(True)
plt.show()

# Draw Q-Q plot for age and body fat percentage
plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1)
stats.probplot(df['age'], dist="norm", plot=plt)
plt.title('Q-Q Plot for Age')

plt.subplot(1, 2, 2)
stats.probplot(df['body_fat_percent'], dist="norm", plot=plt)
plt.title('Q-Q Plot for Body Fat Percentage')

plt.tight_layout()
plt.show()
