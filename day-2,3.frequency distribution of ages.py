import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Generate sample data (ages of customers who made purchases)
np.random.seed(0)
ages = np.random.randint(18, 70, size=100)  # Generating 100 random ages between 18 and 70

# Calculate frequency distribution using pandas
age_counts = pd.Series(ages).value_counts().sort_index()

# Plotting the frequency distribution
plt.figure(figsize=(10, 6))
plt.bar(age_counts.index, age_counts.values, color='skyblue')
plt.title('Frequency Distribution of Customer Ages')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.grid(True)
plt.xticks(age_counts.index)
plt.tight_layout()
plt.show()

# Displaying the frequency distribution as a table
print("Frequency Distribution of Customer Ages:")
print(age_counts)
