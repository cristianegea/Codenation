from uuid import uuid4
# uuid = identificador único universal (objetivo: ser um identificador único para um objeto)

# criação de um dicionário global para manter os dados em memória
_in_memory_storage = dict()

# criação do objeto "save"
def save(data):
    # identificação das listas salvas do dicionário (forma de recuperar depois as informações do dicionário)
    data_uuid = uuid4()
        # uuid para identificar as listas, dados que forem salvos dentro do dicionário (forma de recuperar os dados depois)
        # uuid4 retorna um objeto da classe uuid
        # a chave é um objeto uuid (não é uma string)

    _in_memory_storage[data_uuid] = data
        # data => dado que foi repassado

    return data_uuid

def get(uuid):
    return _in_memory_storage[UUID(uuid)]