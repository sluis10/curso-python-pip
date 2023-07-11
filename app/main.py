import utils
import read_csv
import charts
import pandas as pd


def run():
    #Código para generar el pie chart sin usar PANDAS
    '''
    data = list(filter(lambda item: item['Continent'] == 'South America', data))

    countries = list(map(lambda x: x['Country/Territory'], data))
    percentages = list(map(lambda x: x['World Population Percentage'], data))
    '''
    
    # df(dataframe) 
    df = pd.read_csv('data.csv')
    # Nos ahorramos el método creado read_csv.py, pd.read_csv es un método que transforma el documento a una lista manejable de Python
    df = df[df['Continent'] == 'Africa']
    # Equivalente a -> data = list(filter(lambda item : item['Continent'] == 'Africa',data))

    countries = df['Country/Territory'].values
    # Equivalente a -> countries = list(map(lambda x: x['Country/Territory'], data))
    percentages = df['World Population Percentage'].values
    # Equivalente a -> percentages = list(map(lambda x: x['WorldPopulationPercentage'], data))
    charts.generate_pie_chart(countries, percentages)

    data = read_csv.read_csv('data.csv')
    country = input('Type Country: ')
    result = utils.population_by_country(data, country)
    
    if len(result) > 0:
        country = result[0]
        labels, values = utils.get_population(country)
        charts.generate_bar_chart(country['Country/Territory'], labels, values)


if __name__ == '__main__':
    run()