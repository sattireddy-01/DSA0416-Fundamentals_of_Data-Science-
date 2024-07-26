import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Sample dataset (replace this with your actual dataset)
data = {
    'Smoking': [1, 0, 1, 0, 1, 0, 1, 1, 0, 1], # 1: smoker, 0: non-smoker
    'LungCancerRate': [20, 15, 25, 10, 50, 10, 35, 45, 15, 40] # Incidence of lung cancer per 1000 individuals
}

df = pd.DataFrame(data)

# Calculate correlation coefficient
correlation_coefficient = np.corrcoef(df['Smoking'], df['LungCancerRate'])[0, 1]

print("Correlation Coefficient between Smoking and Lung Cancer Rates:", correlation_coefficient)

# Create scatter plot
plt.figure(figsize=(8, 6))
plt.scatter(df['Smoking'], df['LungCancerRate'], color='blue')
plt.title('Scatter Plot of Smoking vs Lung Cancer Rates')
plt.xlabel('Smoking (1: Smoker, 0: Non-smoker)')
plt.ylabel('Lung Cancer Rates (per 1000 individuals)')
plt.grid(True)
plt.show()
