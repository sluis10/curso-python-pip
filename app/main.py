import utils
import read_csv
import charts


def run():
    data = read_csv.read_csv('data.csv')
    country = input('Type Country: ')
    result = utils.population_by_country(data, country)
    
    if len(result) > 0:
        country = result[0]
        labels, values = utils.get_population(country)
        charts.generate_bar_chart(country['Country/Territory'], labels, values)


if __name__ == '__main__':
    run()


# No funciona lo de mostrar la gráfica, leer lo que puse en charts.py