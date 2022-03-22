import requests


class TestCursos:
    headers = {'Authorization': 'Token 1111d49ebefa698abb1b795376827ce97a0f26d7'}
    url_base_cursos = 'http://127.0.0.1:8000/api/v2/cursos/'

    def test_get_cursos(self):
        resposta = requests.get(url=self.url_base_cursos, headers=self.headers)

        assert resposta.status_code == 200

    def test_get_curso(self):
        resposta = requests.get(url=f'{self.url_base_cursos}9/', headers=self.headers)

        assert resposta.status_code == 200

    def test_post_curso(self):
        novo = {
            'titulo': 'Curso de programacao com Node1',
            'url': 'https://wwww.google.com.br/node2'
        }

        resposta = requests.post(url=self.url_base_cursos, headers=self.headers, data=novo)

        assert resposta.status_code == 201
        assert resposta.json()['titulo'] == novo['titulo']

    def test_put_curso(self):
        atualizado = {
            'titulo': 'Curso de programacao com Node2',
            'url': 'https://wwww.google.com.br/node2'
        }

        resposta = requests.put(url=f'{self.url_base_cursos}9/', headers=self.headers, data=atualizado)

        assert resposta.status_code == 201
        assert resposta.json()['titulo'] == atualizado['titulo']

    def test_delete_curso(self):
        resposta = requests.delete(url=f'{self.url_base_cursos}9/', headers=self.headers)
        assert resposta.status_code == 204 and len(resposta.text) == 0
