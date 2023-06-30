import matplotlib.pyplot as plt
import pandas as pd

from amount_of_death_by_age_graph import amount_of_death_by_age_graph_generator
from death_distribution_chart_according_to_states import death_distribution_chart_generator_according_to_states
from helpers import treat_data
from scatter_plot import draw_scatter_plot
from box_plot import draw_box_plot
from line_plot import draw_line_plot


if __name__ == "__main__":
    # Set graphics size
    plt.rcParams['figure.figsize'] = (11, 7)

    # Reading the data into the program and applying treatment.
    path_of_database = 'dataBase/death_cause_brazil.csv'
    data = pd.read_csv(path_of_database)
    data = treat_data(data)

    # Chart generators
    draw_scatter_plot(data)
    amount_of_death_by_age_graph_generator(data)
    draw_box_plot(data)
    death_distribution_chart_generator_according_to_states(data)
    draw_line_plot(data)

