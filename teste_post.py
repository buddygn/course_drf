import requests


headers = {'Authorization': 'Token 1111d49ebefa698abb1b795376827ce97a0f26d7'}

url_base_cursos = 'http://127.0.0.1:8000/api/v2/cursos/'
url_base_avaliacoes = 'http://127.0.0.1:8000/api/v2/avaliacoes/'

novo_curso = {
    'titulo': 'Gerência Ágil de Projetos com Scrum',
    'url': 'https://www.gapcs.com.br'
}

resultado = requests.post(url_base_cursos, headers=headers, data=novo_curso)

# Testing status code HTTP 201
assert resultado.status_code == 201

# Testing if the title of the created course is the same as the one informed
assert resultado.json()['titulo'] == novo_curso['titulo']
