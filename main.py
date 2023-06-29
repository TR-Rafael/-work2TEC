import matplotlib.pyplot as plt
import csv
import re
import random
import numpy as np

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

def amount_of_death_by_age_graph_generator(payload):
    mortes = list(map(lambda x: '0 - 9' if x == '< 9' else x, payload))
    mortes = list(map(lambda x: '100 - 110' if x == '> 100' else x, mortes))
    mortes = list(map(lambda x: convert_range_to_random(x), mortes))
    plt.xlabel("Idades")
    plt.ylabel("Total de mortes")
    plt.title("Quantidade de mortes por faixa etaria")
    plt.hist(mortes, 30, rwidth=0.9)
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

def graph3(payload):
    mortes = payload
    # Daonde você tirou esses estados bicho? Preciso dessa info para saber como tratar esse código...
    #  Isso aqui foi uma tentativa do gráfico de Barras e colunas
    plt.bar(list(map(lambda x: x['state'], mortes)), height=list(map(lambda x: x['Estados'], mortes)), color='blue')
    plt.xlabel('state')
    plt.ylabel('Estados')
    plt.show()


if __name__ == "__main__":
    #  Eu deixei os nomes dos gráficos que não consegui finalizar genéricos mesmo e quando
    # Conseguirmos fazer, a gente ajeita.
    path_of_database = 'dataBase/death_cause_brazil.csv'
    data = read_csv(path_of_database)
    #  Esse abaixo estata funcionando
    # amount_of_death_by_age_graph_generator(list(map(lambda x: x['age'], data)))

    # Esse a explicação sobre onde parei está dentro da função
    # graph2(data)

    # Esse a explicação sobre onde parei está dentro da função
    # graph3(data)

    #O gráfico de linhas eu acho que sei como fazer, vou tentar amanhã.
