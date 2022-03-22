import requests

headers = {'Authorization': 'Token 1111d49ebefa698abb1b795376827ce97a0f26d7'}

url_base_cursos = 'http://127.0.0.1:8000/api/v2/cursos/8/'


resultado = requests.delete(url_base_cursos, headers=headers)

# Testing status code HTTP 204
assert resultado.status_code == 204

# Testing if body size is 0
assert len(resultado.text) == 0
