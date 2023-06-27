import matplotlib.pyplot as plt
import csv

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

def bar_graph_generator(payload):
    # ['date', 'state', 'gender', 'age', 'color', 'cause', 'total'] <- column_names
    #  TODO Parei aqui, tava testando algumas coisas da plot lib. Por isto esta esse caos
    #   Quando retornar irei tentar fazer um grafico que mostre ao longo dos meses quantos homens e mulheres morreram kkk
    Eixo_x1 = [0.25, 1.25, 2.25, 3.25, 4.25]
    Eixo_y1 = list(filter(lambda x: x['gender'] == 'M', payload))[0:5]
    plt.bar(Eixo_x1, Eixo_y1, label="Man", width=.5)
    #
    Eixo_x2 = [.75, 1.75, 2.75, 3.75, 4.75]
    Eixo_y2 = list(filter(lambda x: x.gender == 'F', payload))[0:5]
    plt.bar(Eixo_x2, Eixo_y2, label="Woman", color='r', width=.5)

    plt.legend()
    plt.xlabel("Dias")
    plt.ylabel("Distância(km)")
    plt.title("Informação")
    plt.show()


if __name__ == "__main__":
    path_of_database = 'dataBase/death_cause_brazil.csv'

    # for value in lerCSV(path_of_database):
    #     print(value)
    bar_graph_generator(read_csv(path_of_database))
    print('Executou')
