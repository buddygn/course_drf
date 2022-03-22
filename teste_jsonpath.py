import requests
import jsonpath

headers = {'Authorization': 'Token 1111d49ebefa698abb1b795376827ce97a0f26d7'}
avaliacoes = requests.get(url='http://127.0.0.1:8000/api/v2/avaliacoes/')

# resultados = jsonpath.jsonpath(avaliacoes.json(), 'results')
# print(resultados)

# primeira = jsonpath.jsonpath(avaliacoes.json(), 'results[0]')
# print(primeira)
#
# nome = jsonpath.jsonpath(avaliacoes.json(), 'results[0].nome')
# print(nome)


nomes = jsonpath.jsonpath(avaliacoes.json(), 'results[*].avaliacao')
print(nomes)
