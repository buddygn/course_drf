import requests

headers = {'Authorization': 'Token 1111d49ebefa698abb1b795376827ce97a0f26d7'}

url_base_cursos = 'http://127.0.0.1:8000/api/v2/cursos/8/'
url_base_avaliacoes = 'http://127.0.0.1:8000/api/v2/avaliacoes/'

curso_atualizado = {
    'ativo': True,
    'titulo': 'Gerência Ágil de Projetos com Scrum1',
    'url': 'https://www.gapcs.com.br'

}

resultado = requests.put(url_base_cursos, headers=headers, data=curso_atualizado)

# Testing status code HTTP 200
assert resultado.status_code == 200

# Testing if the course update active information
assert resultado.json()['ativo'] is True

