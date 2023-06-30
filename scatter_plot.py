import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from adjustText import adjust_text

def draw_scatter_plot(data: pd.DataFrame):
    subset_2019 = data[data['date'] <= '2019-09-15']
    subset_2020 = data[data['date'] >= '2020-01-01']

    subset_2019_grouped_by_cause = subset_2019.groupby('cause')['total'].sum().reset_index()
    subset_2020_grouped_by_cause = subset_2020.groupby('cause')['total'].sum().reset_index()
    result = pd.merge(subset_2020_grouped_by_cause, subset_2019_grouped_by_cause, on='cause', how='left')

    result.fillna(0, inplace=True)

    result = result[~result['cause'].isin(['Others', 'Undetermined'])]

    plt.scatter(result['total_x'], result['total_y'], color='blue')
    plt.plot(np.unique(result['total_x']),
             np.poly1d(np.polyfit(result['total_x'], result['total_y'], 1))(
                 np.unique(result['total_x'])), color='red')
    plt.xlabel('Mortes em 2020')
    plt.ylabel('Mortes em 2019')

    ax = sns.scatterplot(x='total_x', y='total_y', data=result, color='blue')
    texts = []
    for i, row in result.iterrows():
        texts.append(ax.text(row['total_x'], row['total_y'], row['cause'], ha='center', va='bottom', fontsize=8))

    adjust_text(texts)
    plt.show()
