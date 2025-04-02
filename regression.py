import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Load the standardized data
FILENAME_INPUT = "data/report_2018-2019_standardized.csv"
df = pd.read_csv(FILENAME_INPUT)

# Define features and target
features = [
    "GDP per capita",
    "Social support",
    "Healthy life expectancy",
    "Freedom to make life choices",
    "Generosity",
    "Perceptions of corruption"
]
X = df[features]
y = df["Score"]  # Happiness Score is NOT standardized

# Train linear regression model
model = LinearRegression()
model.fit(X, y)

# Get coefficients and R²
coefficients = pd.Series(
    model.coef_, index=features).sort_values(ascending=True)
r_squared = model.score(X, y)

# Print results
print("Linear Regression Coefficients:")
print(coefficients.sort_values(ascending=False))
print(f"\nR² Score: {r_squared:.3f}")

# Plot coefficients
plt.figure(figsize=(8, 6))
coefficients.plot(kind='barh')
plt.title("Feature Impact on Happiness Score")
plt.xlabel("Regression Coefficient")
plt.grid(True)
plt.tight_layout()
plt.show()
