from sklearn.preprocessing import StandardScaler
import pandas as pd

FILENAME_INPUT = "data/report_2018-2019.csv"
FILENAME_OUTPUT = FILENAME_INPUT.replace(".csv", "_standardized.csv")

# Load the dataset
df = pd.read_csv(FILENAME_INPUT)

# Columns to standardize
features_to_scale = [
    "GDP per capita",
    "Social support",
    "Healthy life expectancy",
    "Freedom to make life choices",
    "Generosity",
    "Perceptions of corruption"
]

# Create a copy of the original DataFrame
df_scaled = df.copy()

# Standardize the features
scaler = StandardScaler()
df_scaled[features_to_scale] = scaler.fit_transform(
    df_scaled[features_to_scale])

# Save the standardized DataFrame to a new CSV file
df_scaled.to_csv(FILENAME_OUTPUT, index=False)
print(f"Standardized data saved to {FILENAME_OUTPUT}")
