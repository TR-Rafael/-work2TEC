import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def draw_box_plot(data: pd.DataFrame):
    filtered_data = data[data['color'] != "Ignored"]

    plt.figure(figsize=(8, 6))
    sns.boxplot(x=filtered_data['color'], y=filtered_data['age'], color='#add8e6')

    plt.xlabel('Etinia')
    plt.ylabel('Idade da Morte')
    plt.show()
