import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def draw_box_plot(data: pd.DataFrame):
    # Filter the data excluding "Ignored" color
    filtered_data = data[data['color'] != "Ignored"]

    # Create the box plot
    # Create the box plot using Seaborn
    plt.figure(figsize=(8, 6))
    sns.boxplot(x=filtered_data['color'], y=filtered_data['age'], color='#add8e6')

    # Set the labels and title
    plt.xlabel('Etinia')
    plt.ylabel('Idade da Morte')

    # Display the plot
    plt.show()
