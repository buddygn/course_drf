import requests


headers = {'Authorization': 'Token 1111d49ebefa698abb1b795376827ce97a0f26d7'}

url_base_cursos = 'http://127.0.0.1:8000/api/v2/cursos/'
url_base_avaliacoes = 'http://127.0.0.1:8000/api/v2/avaliacoes/'

resultado = requests.get(url=url_base_cursos, headers=headers)

# Testing if the endpoint is correct
assert resultado.status_code == 200

# Testing the amount of data
assert resultado.json()['count'] == 3
