import requests
from bs4 import BeautifulSoup

# URL de la página a la que haremos scraping
url = "https://larepublica.pe/"

# Realizar la solicitud HTTP GET a la página
response = requests.get(url)

# Verificar que la solicitud fue exitosa (código 200)
if response.status_code == 200:
    # Crear el objeto BeautifulSoup con el contenido de la página
    soup = BeautifulSoup(response.text, 'html.parser')
    
    print(soup)

    # Buscar el título de la página
    titulo = soup.title.string
    
    # Imprimir el título de la página
    print(f"El título de la página es: {titulo}")
else:
    print(f"Error al acceder a la página. Código de estado: {response.status_code}")
