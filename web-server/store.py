import requests


def get_categories():
    r = requests.get('https://api.escuelajs.co/api/v1/categories')
    print(r.status_code)  # El estado
    print(r.text)  # La información del API
    print(type(r.text))
    categories = r.json()
    print(type(categories))

    for category in categories:
        print(category['name'])