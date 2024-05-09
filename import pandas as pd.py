import pandas as pd

from google.colab import drive
drive.mount('/content/drive')

file_path = '/content/drive/MyDrive/CarsData.csv'

data = pd.read_csv(file_path)

data.head(n=50)

# @title price vs mileage

from matplotlib import pyplot as plt
data.plot(kind='scatter', x='price', y='mileage', s=32, alpha=.8)
plt.gca().spines[['top', 'right',]].set_visible(False)

avg_mpg_by_year = data.groupby('year')['mpg'].mean().reset_index()

import seaborn as sns

sns.lineplot(data=avg_mpg_by_year, x='year', y='mpg', marker='o')
sns.despine(false)
sns.set_context("talk")
sns.set_palette("pastel")
sns.set_style("white")

avg_mpg_by_year.to_csv('avg_mpg_by_year.csv', index=False)