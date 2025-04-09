import pandas as pd
import matplotlib.pyplot as plt

# XAxis = "GDP per capita"
# XAxis = "Social support"
# XAxis = "Healthy life expectancy"
# XAxis = "Perceptions of corruption"
XAxis = "Generosity"

YAxis = "Score"
DATAFILE = "./data/report_2018-2019.csv"

# Last inn CSV-data
df = pd.read_csv(DATAFILE)

# Ta snittet per land (flere år per land)
mean_df = df.groupby("Country or region",
                     as_index=False).mean(numeric_only=True)

# Sorter etter GDP per capita
mean_df_sorted = mean_df.sort_values(XAxis, ascending=True)


# Plotting
plt.figure(figsize=(12, 6))
plt.bar(mean_df_sorted["Country or region"], mean_df_sorted[YAxis],
        align='edge',
        width=0.75,
        edgecolor='none')

if YAxis == "Score":
    YAxis = "Happiness Score"

plt.title(YAxis + " vs " + XAxis+" (sorted)")
plt.xlabel(XAxis)
plt.ylabel(YAxis)
plt.xticks(rotation=90, fontsize=6)
plt.grid(axis='y')

plt.xlim(-0.5, len(mean_df_sorted) - 0.5)
plt.tight_layout()
plt.show()
