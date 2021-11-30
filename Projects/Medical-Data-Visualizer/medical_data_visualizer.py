import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Import data
df = pd.read_csv('medical_examination.csv')

# Add 'overweight' column
BMI = df['weight'].values / ((df['height'].values / 100) ** 2)
df['overweight'] = (BMI > 25).astype(int)

# Normalize data by making 0 always good and 1 always bad. If the value of 'cholesterol' or 'gluc' is 1, make the value 0. If the value is more than 1, make the value 1.
df[['cholesterol', 'gluc']] = (~(df[['cholesterol', 'gluc']].values == 1)).astype(int)

# Draw Categorical Plot
def draw_cat_plot():
  # Create DataFrame for cat plot using `pd.melt` using just the values from 'cholesterol', 'gluc', 'smoke', 'alco', 'active', and 'overweight'.
  df_cat = pd.melt(df, id_vars=['cardio'], value_vars=['cholesterol', 'gluc', 'smoke', 'alco', 'active', 'overweight'])

  # Group and reformat the data to split it by 'cardio'. Show the counts of each feature. You will have to rename one of the columns for the catplot to work correctly.
  df_cat = df_cat.groupby(['cardio', 'variable', 'value'])['value'].count().to_frame()
  df_cat.rename(columns={'value': 'total'}, inplace=True)
  df_cat.reset_index(inplace=True)

  # Draw the catplot with 'sns.catplot()'
  catplot = sns.catplot(x='variable', y='total', hue='value', col='cardio', kind='bar', data=df_cat)
  fig = catplot.fig

  # Do not modify the next two lines
  fig.savefig('catplot.png')
  return fig

# Draw Heat Map
def draw_heat_map():
  # Clean the data
  df_heat = df[df['ap_lo'] <= df['ap_hi']]
  df_heat = df_heat[df_heat['height'] >= (df['height'].quantile(0.025))]
  df_heat = df_heat[df_heat['height'] <= (df['height'].quantile(0.975))]
  df_heat = df_heat[df_heat['weight'] >= (df['weight'].quantile(0.025))]
  df_heat = df_heat[df_heat['weight'] <= (df['weight'].quantile(0.975))]

  # Calculate the correlation matrix
  corr = df_heat.corr().round(1)

  # Generate a mask for the upper triangle
  mask = np.triu(np.ones_like(corr, dtype=bool))

  # Set up the matplotlib figure
  fig, ax = plt.subplots(figsize=(12,9))

  # Draw the heatmap with 'sns.heatmap()'
  heat_map = sns.heatmap(corr, mask=mask, annot=True, fmt=".1f", square=True)
  heat_map.set_yticklabels(heat_map.get_yticklabels(), rotation=0)
  heat_map.set_xticklabels(heat_map.get_xticklabels(), rotation=90)

  # Do not modify the next two lines
  fig.savefig('heatmap.png')
  return fig