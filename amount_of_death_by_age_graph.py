import pandas as pd
from matplotlib import pyplot as plt


def amount_of_death_by_age_graph_generator(data: pd.DataFrame):
    plt.xlabel("Idades")
    plt.ylabel("Total de mortes")
    plt.title("Quantidade de mortes por faixa etaria")
    plt.hist(data['age'], bins=30, rwidth=0.9)
    plt.show()
