def get_population(country_dict):
    '''
    population_dict = {
    '2022': int(country_dict['2022 Population']),
    '2020': int(country_dict['2020 Population']),
    '2015': int(country_dict['2015 Population']),
    '2010': int(country_dict['2010 Population']),
    '2000': int(country_dict['2000 Population']),
    '1990': int(country_dict['1990 Population']),
    '1980': int(country_dict['1980 Population']),
    '1970': int(country_dict['1970 Population'])
    }
    '''
    population_dict = {key[:4]: int(value) for key, value in country_dict.items() if key[:4].isdigit() == True} # Este lo hice yo, el de arriba es del video
    
    labels = population_dict.keys()
    values = population_dict.values()
    return labels, values

def population_by_country(data, country):
    result = list(filter(lambda item: item['Country/Territory'] == country, data))
    return result

def world_population_percentage(data):
    country = list(map(lambda item: item['Country/Territory'], data)) #labels
    population = list(map(lambda item: float(item['World Population Percentage']), data)) #values
    return country, population