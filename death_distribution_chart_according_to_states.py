import pandas as pd
from matplotlib import pyplot as plt


def death_distribution_chart_generator_according_to_states(data: pd.DataFrame):
    death_by_states = data['state'].value_counts().sort_index()
    plt.bar(death_by_states.index, death_by_states.values, label="Mortes por estado", width=0.35)
    plt.legend()
    plt.xlabel("Estados")
    plt.ylabel("Número de Mortes")
    plt.title("Distribuição de mortes por estados")
    plt.show()
