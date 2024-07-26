import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats as stats

# Creating a DataFrame with age and %fat data
data = {
    'age': [23, 23, 27, 27, 39, 41, 47, 49, 50, 52, 54, 54, 56, 57, 58, 58, 60, 61],
    '%fat': [9.5, 26.5, 7.8, 17.8, 31.4, 25.9, 27.4, 27.2, 31.2, 34.6, 42.5, 28.8, 33.4, 30.2, 34.1, 32.9, 41.2, 35.7]
}

df = pd.DataFrame(data)

# Calculate mean, median, and standard deviation
mean_age = df['age'].mean()
median_age = df['age'].median()
std_age = df['age'].std()

mean_fat = df['%fat'].mean()
median_fat = df['%fat'].median()
std_fat = df['%fat'].std()

# Draw boxplots
plt.figure(figsize=(10, 6))
plt.subplot(1, 2, 1)
df.boxplot(column=['age'])
plt.title('Boxplot of Age')

plt.subplot(1, 2, 2)
df.boxplot(column=['%fat'])
plt.title('Boxplot of %Fat')

plt.tight_layout()
plt.show()

# Draw scatter plot
plt.figure(figsize=(8, 6))
plt.scatter(df['age'], df['%fat'])
plt.title('Scatter Plot of Age vs %Fat')
plt.xlabel('Age')
plt.ylabel('%Fat')
plt.grid(True)
plt.show()

# Draw Q-Q plot
plt.figure(figsize=(8, 6))
stats.probplot(df['age'], dist="norm", plot=plt)
plt.title('Q-Q Plot of Age')
plt.xlabel('Theoretical Quantiles')
plt.ylabel('Sample Quantiles')
plt.grid(True)
plt.show()

plt.figure(figsize=(8, 6))
stats.probplot(df['%fat'], dist="norm", plot=plt)
plt.title('Q-Q Plot of %Fat')
plt.xlabel('Theoretical Quantiles')
plt.ylabel('Sample Quantiles')
plt.grid(True)
plt.show()

# Output the calculated statistics
print("Age:")
print("Mean:", mean_age)
print("Median:", median_age)
print("Standard Deviation:", std_age)

print("\n%Fat:")
print("Mean:", mean_fat)
print("Median:", median_fat)
print("Standard Deviation:", std_fat)
