import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the standardized dataset
FILENAME_INPUT = "data/report_2018-2019_standardized.csv"
df = pd.read_csv(FILENAME_INPUT)

# Define features to compare with Score
features = [
    "GDP per capita",
    "Social support",
    "Healthy life expectancy",
    "Freedom to make life choices",
    "Generosity",
    "Perceptions of corruption",
    "Score"
]

# Calculate the Pearson correlation matrix
corr_matrix = df[features].corr(method='pearson')

# Print the correlation matrix
print("Full Pearson Correlation Matrix:\n")
print(corr_matrix.round(2))

# Plot heatmap
plt.figure(figsize=(10, 8))
sns.heatmap(corr_matrix, annot=True, cmap="RdYlGn", fmt=".2f", square=True)
plt.title("Pearson Correlation Matrix")
plt.tight_layout()
plt.show()
