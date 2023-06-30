import matplotlib.pyplot as plt
import csv
import re
import random
import numpy as np
import pandas as pd
from scatter_plot import draw_scatter_plot
from box_plot import draw_box_plot
from line_plot import draw_line_plot

def read_csv(pathName):
    payload = []
    column_names = []
    with open(pathName, 'r') as fileCSV:
        reader = csv.reader(fileCSV, delimiter=',', quotechar='"')
        for index, line in enumerate(reader):
            if index == 0:
                print(line)
                column_names = line
                continue
            else:
                line_content = {}
                for idx, key in enumerate(column_names):
                    line_content[key] = line[idx]
                payload.append(line_content)

    return payload

def amount_of_death_by_age_graph_generator(data: pd.DataFrame):

    plt.xlabel("Idades")
    plt.ylabel("Total de mortes")
    plt.title("Quantidade de mortes por faixa etaria")
    plt.hist(data['age'], bins=30, rwidth=0.9)
    plt.show()


def convert_range_to_random(range_string):
    range_values = re.findall(r'\d+', range_string)
    if len(range_values) == 2:
        start = int(range_values[0])
        end = int(range_values[1])
        if not any(np.isnan([start, end])):
            return random.sample(range(start, end + 1), 1)[0]
    return np.nan


def graph2(payload):
    #  Não ta funfando... Foi uma tentativa de adaptar o gráfico de Idade das mortes de acordo com as etinias
    #  Com Boxplot, eu tentei ler essa DOC, mas não ajudou muito https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html
    #  Acho que não da pra fazer esse tipo de gráfico na matplot, mas temos que investigar mais...
    mortes = list(filter(lambda x: x['color'] != 'Ignored', payload))
    plt.figure()
    plt.boxplot(list(map(lambda x: x['age'], mortes)))
    plt.xlabel("Etinia")
    plt.ylabel("Idade da Morte")
    plt.show()


def death_distribution_chart_generator_according_to_states(data: pd.DataFrame):
    death_by_states = data['state'].value_counts().sort_index()

    # Create the bar plot
    plt.bar(death_by_states.index, death_by_states.values, label="Mortes por estado", width=0.35)
    plt.legend()
    plt.xlabel("Estados")
    plt.ylabel("Número de Mortes")
    plt.title("Distribuição de mortes por estados")
    plt.show()

def treat_data(df: pd.DataFrame):
    replace_dict = {'< 9': '0 - 9', '> 100': '100 - 110'}
    df["age"].replace(replace_dict, inplace=True)

    # Apply the convert_range_to_random function to the 'age' column
    df["age"] = df["age"].apply(convert_range_to_random)
    return df


if __name__ == "__main__":
    #  Eu deixei os nomes dos gráficos que não consegui finalizar genéricos mesmo e quando
    # Conseguirmos fazer, a gente ajeita.
    plt.rcParams['figure.figsize'] = (11, 7)
    path_of_database = 'dataBase/death_cause_brazil.csv'
    data = pd.read_csv(path_of_database)
    # data = treat_data(data)

    # draw_box_plot(data)
    # draw_scatter_plot(data)
    # death_distribution_chart_generator_according_to_states(data)
    # amount_of_death_by_age_graph_generator(data)
    draw_line_plot(data)
    #  Esse abaixo estata funcionando
    # age_columns = list(map(lambda x: x['age'], data))
    # amount_of_death_by_age_graph_generator(age_columns)

    # Esse a explicação sobre onde parei está dentro da função
    # graph2(data)

    #  Esse abaixo estata funcionando
    # state_columns = list(map(lambda x: x['state'], data))
    # death_distribution_chart_generator_according_to_states(state_columns)

    # O gráfico de linhas eu acho que sei como fazer, vou tentar amanhã.
