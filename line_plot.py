import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

def draw_line_plot(data: pd.DataFrame):
    # Filter the data
    filtered_data = data[data['state'].isin(['RJ', 'SP', 'MG', 'ES'])]
    filtered_data = filtered_data[filtered_data['cause'].str.contains('Covid')]

    # Aggregate the data
    data_agg = filtered_data.groupby(['state', 'date']).agg({'total': 'sum'}).reset_index()
    data_agg['cumulative_deaths'] = data_agg.groupby('state')['total'].cumsum()

    # Create the line graph
    plt.figure(figsize=(10, 6))
    months = mdates.MonthLocator()  # Set the tick locator to months
    month_fmt = mdates.DateFormatter('%b')  # Format the tick labels to display only the month abbreviation

    for state in ['RJ', 'SP', 'MG', 'ES']:
        state_data = data_agg[data_agg['state'] == state]
        plt.plot(state_data['date'], state_data['cumulative_deaths'], label=state)

    plt.xlabel('Data')
    plt.ylabel('Mortes acumuladas')
    plt.title('Mortes acumuladas por estado')
    plt.legend()
    plt.xticks(rotation=45)

    # Set the x-axis tick locators and labels
    plt.gca().xaxis.set_major_locator(months)
    plt.gca().xaxis.set_major_formatter(month_fmt)

    plt.tight_layout()
    plt.show()
