import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

def draw_line_plot(data: pd.DataFrame):
    filtered_data = data[data['state'].isin(['RJ', 'SP', 'MG', 'ES'])]
    filtered_data = filtered_data[filtered_data['cause'].str.contains('Covid')]

    data_agg = filtered_data.groupby(['state', 'date']).agg({'total': 'sum'}).reset_index()
    data_agg['cumulative_deaths'] = data_agg.groupby('state')['total'].cumsum()

    plt.figure(figsize=(10, 6))
    months = mdates.MonthLocator()
    month_fmt = mdates.DateFormatter('%b')

    for state in ['RJ', 'SP', 'MG', 'ES']:
        state_data = data_agg[data_agg['state'] == state]
        plt.plot(state_data['date'], state_data['cumulative_deaths'], label=state)

    plt.xlabel('Data')
    plt.ylabel('Mortes acumuladas')
    plt.title('Mortes acumuladas por Covid nos estados do sudeste em 2020')
    plt.legend()
    plt.xticks(rotation=45)

    plt.gca().xaxis.set_major_locator(months)
    plt.gca().xaxis.set_major_formatter(month_fmt)

    plt.tight_layout()
    plt.show()
