import requests
from requests.models import Response



URL: str = 'https://api.chucknorris.io/jokes/random'


# Realizamos petición y obtenemos la respuesta
respuesta: Response = requests.get(url=URL)

# Comprpbamos el estado HTTP
estado: int = respuesta.status_code

# Obtenemos los datos de la respuesta JSON
datos_json = respuesta.json()


if estado == 200:
    # Obtenemos el chiste de la respuesta accediendo a la clave "Value"
    frase_chuck: str = datos_json['value']
    print(f'El Chiste: {frase_chuck}')




