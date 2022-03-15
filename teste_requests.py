import requests

# GET Avaliacoes
headers = {'Authorization': 'Token 1111d49ebefa698abb1b795376827ce97a0f26d7'}
avaliacoes = requests.get(url='http://127.0.0.1:8000/api/v2/cursos/', headers=headers)

print(avaliacoes.json())