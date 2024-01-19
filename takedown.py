import requests
import os
import sys

# Definir códigos de color ANSI
GREEN = '\033[92m'
RED = '\033[91m'
ENDC = '\033[0m'

def open_webpage(url):
    os.system(f'xdg-open {url}')

def check_website_status(url, user_agent=None):
    headers = {'User-Agent': user_agent} if user_agent else {}
    
    try:
        response = requests.get(url, headers=headers, timeout=5)
        response.raise_for_status()  # Lanza una excepción para errores HTTP (4xx y 5xx)
        
        status_message = f'{urls.index(url) + 1}. La URL {url} está en línea. Código de estado: {response.status_code}'
        
        if response.status_code == 200:
            status_message = f'{GREEN}{status_message}{ENDC}'
            with open('online.txt', 'a') as online_file:
                online_file.write(url + '\n')
            open_webpage(url)  # Abre la URL en el navegador predeterminado
        
        print(status_message)
        
    except requests.exceptions.RequestException:
        print(f'{urls.index(url) + 1}. La URL {url} está fuera de línea.')
    except Exception as e:
        pass  # Oculta otros errores para cumplir con tus requisitos

if __name__ == "__main__":
    try:
        with open('urls.txt', 'r') as file:
            urls = file.read().splitlines()
            
        if not urls:
            print("No se encontraron URLs en el archivo 'urls.txt'.")
            exit()

        print("Opciones de User-Agent:")
        print("1. User-Agent Predeterminado")
        print("2. User-Agent Personalizado")
        
        user_agent_option = input("Seleccione una opción para el User-Agent (1 o 2): ")

        if user_agent_option == '1':
            user_agent = None
        elif user_agent_option == '2':
            user_agent = input("Ingrese su User-Agent personalizado: ")
        else:
            print("Opción no válida para User-Agent. Se utilizará el User-Agent predeterminado.")
            user_agent = None

        for url in urls:
            check_website_status(url, user_agent)
    
    except FileNotFoundError:
        print("El archivo 'urls.txt' no fue encontrado.")
    except Exception as ex:
        pass  # Oculta otros errores para cumplir con tus requisitos
