import requests

# Este módulo contém uma função para buscar dados de usuários de uma API pública.

def fetch_users():
    
    url = "https://jsonplaceholder.typicode.com/users"
    try:
        response = requests.get(url)
        response.raise_for_status() 
        return response.json()
    except requests.RequestException as e:
        print("Erro ao buscar dados da API:", e)
        return None