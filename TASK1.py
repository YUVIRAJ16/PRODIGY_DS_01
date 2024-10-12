

import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
file_path = 'worldpopulationdata1.csv'
data = pd.read_csv(file_path)

# Select the countries to visualize (we'll take the first 10 countries for a cleaner comparison)
countries = data['Country Name'].head(10)
years = ['2022', '2020', '2018', '2015', '2010']

# Extract population data for the selected years
population_data = data[['Country Name'] + years].head(10).set_index('Country Name')

# Plotting the bar chart
population_data.plot(kind='bar', figsize=(12, 6), width=0.8)

# Adding chart details
plt.title('Population Comparison of Countries Across 5 Years', fontsize=16)
plt.ylabel('Population', fontsize=12)
plt.xlabel('Country', fontsize=12)
plt.xticks(rotation=45, ha='right')
plt.tight_layout()

# Show the plot
plt.show()

import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
file_path = 'worldpopulationdata1.csv'
data = pd.read_csv(file_path)

# Select the years of interest
years = ['2022', '2021', '2020', '2019', '2018']

# Extract population data for the selected years and sort by 2022 population
top_countries = data[['Country Name'] + years].sort_values(by='2022', ascending=False).head(10).set_index('Country Name')

# Plotting the bar chart
top_countries.plot(kind='bar', figsize=(12, 6), width=0.8)

# Adding chart details
plt.title('Top 10 Countries by Population (2018-2022)', fontsize=16)
plt.ylabel('Population', fontsize=12)
plt.xlabel('Country', fontsize=12)
plt.xticks(rotation=45, ha='right')
plt.tight_layout()

# Show the plot
plt.show()

import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
file_path = 'worldpopulationdata1.csv'
data = pd.read_csv(file_path)

# Select the years of interest
years = ['2022', '2021', '2020', '2019', '2018']

# Extract population data for the selected years and sort by 2022 population
bottom_countries = data[['Country Name'] + years].sort_values(by='2022', ascending=True).head(10).set_index('Country Name')

# Plotting the bar chart
bottom_countries.plot(kind='bar', figsize=(12, 6), width=0.8)

# Adding chart details
plt.title('Bottom 10 Countries by Population (2018-2022)', fontsize=16)
plt.ylabel('Population', fontsize=12)
plt.xlabel('Country', fontsize=12)
plt.xticks(rotation=45, ha='right')
plt.tight_layout()

# Show the plot
plt.show()