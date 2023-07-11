import store
from fastapi import FastAPI
from fastapi.responses import HTMLResponse


app = FastAPI() #Instancia de FastAPI

@app.get('/') #Funcion decorada: Cada que se obtenga la ruta '/'se ejecutara la siguiente funcion
def get_list():
    return [1, 2, 3] #Devolverá una lista de numeros

@app.get('/contact', response_class=HTMLResponse) #Funcion decorada: Cada que se obtenga la ruta '/contact' tendra una respuesta de tipo HTMl
def get_list():                                   #Esto es para que pueda soportar una solicitud HTML y funcione la pagina
    return """
        <h1>Hola soy una pagina</h1>
        <p>soy un parrafo</p>
    """

def run():
    store.get_categories()


if __name__ == '__main__':
    run()