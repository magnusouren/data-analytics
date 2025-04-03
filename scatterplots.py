import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the standardized data
FILENAME_INPUT = "data/report_2018-2019_standardized.csv"
df = pd.read_csv(FILENAME_INPUT)

# Define features to compare with Score
features = [
    "GDP per capita",
    "Social support",
    "Healthy life expectancy",
    "Freedom to make life choices",
    "Generosity",
    "Perceptions of corruption"
]

# Plot settings
plt.figure(figsize=(18, 12))
sns.set(style="whitegrid")

# Create scatter plots with linear trend lines
for i, feature in enumerate(features, 1):
    plt.subplot(2, 3, i)
    plt.xlim(-3, 3)
    plt.ylim(0, 8)
    sns.regplot(data=df,
                x=feature,
                y="Score",
                scatter_kws={'alpha': 0.4},
                line_kws={'color': 'black', 'alpha': 0.7},
                ci=None,
                truncate=False
                )
    plt.title(f"{feature} vs Happiness Score")
    plt.xlabel(feature)
    plt.ylabel("Happiness Score")

plt.tight_layout()
plt.show()
