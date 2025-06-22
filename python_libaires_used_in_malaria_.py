import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import warnings 

#                                                          ✨ THE FILE LINK ✨                                       
df = pd.read_csv(r"C:\Users\DELL\Downloads\442CEA8_ALL_LATEST (1).csv")

#                                    DISPLAY BASIC INFORMATION AND SUMMARY
print("THE INFO ABOUT THE FILE:\n",df.info())
print(df.describe())

#                                      CHECKING NUMBER OF MISSING VALUES
print("THE NULL VALUES IN THE FILE ARE: \n",df.isnull().sum())


#                                1. SCATTER PLOT: MALARIA INCIDENCE RATES OVER TIME (UGANDA)
df_uganda = df[df['GEO_NAME_SHORT'] == 'Uganda']
plt.figure(figsize=(10, 6))
sns.scatterplot(x='DIM_TIME', y='RATE_PER_1000_N', data=df_uganda, color='blue', s=100)
plt.xlabel('Year')
plt.ylabel('Malaria Incidence Rate per 1000')
plt.title('Trend of Malaria Incidence Rates in Uganda (2000-2022)')
plt.grid(True)
plt.show()

#                                 2. LINE CHART: MALARIA INCIDENCE TRENDS OVER TIME (GLOBAL)
df_global = df[df['DIM_GEO_CODE_TYPE'] == 'GLOBAL']
plt.figure(figsize=(10, 6))
sns.lineplot(x='DIM_TIME', y='RATE_PER_1000_N', data=df_global, marker='o', color='green')
plt.xlabel('Year')
plt.ylabel('Malaria Incidence Rate per 1000')
plt.title('Global Trend of Malaria Incidence Rates (2000-2022)')
plt.grid(True)
plt.show()

#                              3. HEATMAP: MALARIA INCIDENCE RATES BY REGION AND YEAR
df_regions = df[df['DIM_GEO_CODE_TYPE'] == 'REGION']
heatmap_data = df_regions.pivot_table(index='GEO_NAME_SHORT', columns='DIM_TIME', values='RATE_PER_1000_N')
plt.figure(figsize=(12, 8))
sns.heatmap(heatmap_data, cmap='YlOrRd', annot=True, fmt=".1f", linewidths=0.5)
plt.xlabel('Year')
plt.ylabel('Region')
plt.title('Malaria Incidence Rates by Region and Year')
plt.tight_layout()
plt.show()


#                       4. HISTOGRAM: DISTRIBUTION OF MALARIA INCIDENCE RATES (GLOBAL)
plt.figure(figsize=(10, 6))
sns.histplot(df['RATE_PER_1000_N'], bins=30, kde=True, color='purple')
plt.xlabel('Malaria Incidence Rate per 1000')
plt.ylabel('Frequency')
plt.title('Distribution of Malaria Incidence Rates (Global)')
plt.show()

#               5. BOX PLOT: DISTRIBUTION OF MALARIA INCIDENCE RATES BY REGION
df_regions = df[df['DIM_GEO_CODE_TYPE'] == 'REGION']
plt.figure(figsize=(12, 8))
sns.boxplot(x='GEO_NAME_SHORT', y='RATE_PER_1000_N', data=df_regions, palette="Spectral")
plt.xlabel('Region')
plt.ylabel('Malaria Incidence Rate per 1000')
plt.title('Distribution of Malaria Incidence Rates by Region')
plt.xticks(rotation=90)
plt.show()


