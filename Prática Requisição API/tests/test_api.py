import pytest
import requests

'''
Para buscar uma informação, esta tem que ter sido salva antes. Para isso, eu preciso de alguma forma salvar o dado antes
para, então, pegar o uuid dele.
'''
'''
default: sempre antes de executar algum método de teste (como os abaixo), o pytest vai executar o método da "fixture"
(no caso, método "uuid").
O "uuid" não começa com "test", mas com "def" => não é um teste, mas uma fixture"
'''

class TestAPI:
    @pytest.fixture
    def url(self):
        return "http://localhost:5000/data"

    @pytest.fixture
    def data(self):
        return [1, 2, 3, 4]

    @pytest.fixture
    # uma feature pode entrar dentro de outra feature
    # criação do método uuid (este método vai retornar um uuid de algo válido que já está salvo no API e diposnível para uso)
    # este método é executado primeiramente
    def uuid(self, url, data):
        response = requests.post(url, json={'data': data})

        return response.json()["uuid"]

    def test_save_data(self, uuid):
        # verifica se o método não é nulo
        assert uuid is not None

'''
Antes de executar o "test_get_data()", o pytest vai executar o "uuid()", vai pegar o valor de retorno ("return"), que no
caso é o valor da "uuid", e vai utilizar como argumento para o "test_get_data()" => isso permite injeção de dependências
'''

    def test_get_data(self, url, uuid, data):
        # requisição do "get_data" (já tenho uma "uuid" válida)
        response = requests.get(url + f"/{uuid}")

        assert response.ok
        assert response.json()["data"] == data

    def test_calc_mean(self, url, uuid):
        response = requests.get(url + f"/{uuid}/mean")

        assert response.ok
        assert response.json()["result"] == pytest.approx(2.5)

def test_calc_min(self, url, uuid):
    response = requests.get(url + f"/{uuid}/min")

    assert response.ok
    assert response.json()["result"] == pytest.approx(1)

def test_calc_max(self, url, uuid):
        response = requests.get(url + f"/{uuid}/max")

        assert response.ok
        assert response.json()["result"] == pytest.approx(4)

# como os testes são parecidos, é possível parametrizá-los
@pytest.mark.parametrize("operation, expected_result", [("mean", 2.5), ("min", 1), ("max", 4)])
def test_calc_parametrized(self, uuid, operation, expected_result):
    response = requests.get(url + f"/{uuid}/{operation}")

    assert response.ok
    assert response.json()["result"] == pytest.approx(expected_result)

