'''
Elaboração de uma API rest
Objetivo: submeter uma lista para API, que guarda esta lista na memória, possibilitando a realização de algumas operações

Boas práticas => fazer 3 blocos de import
    * Bloco 1: todos os imports das bibliotecas padrão do python (bibliotecas nativas)
    * Bloco 2: todas as bibliotecas de terceiros (bibliotecas que precisam ser instaladas por meio do "pip install")
    * Bloco 3: os módulos/pacotes criados no próprio projeto
'''

# Importação das bibliotecas de terceiros
from flask import Flask, request, jsonify
from loguru import logger
    # loguru => framework de log (sem muito setup)

# Importação das bibliotecas de terceiros
from statsapi import data_store
from statsapi import operation

# Criação do aplicativo principal
app = Flask(__name__)

#  1º endpoint do API (objetivo: guardar a lista que vou receber)
@app.route("/data", method = ["POST"])
def save_data():
    # configuração do log
    logger.info(f"Saving Data...")

    # conteúdo da requisição (no formato json)
    content = request.get_json()

    # armazenamento dos dados (mais especificamente, das informações contidas no campo "data")
    uuid = data_store.save(content["data"])
        # o "data_store" retornará um "uuid" (identificador do dado salvo na API)

    logger.info(f"Data saved with wid '{uuid}' successfully")

    return jsonify({"status": "success", "message": "data saved successfully", "uuid": uuid})

#  Endpoint para buscar os dados da API
@app.route("/data/<uuid>", method = ["GET"])
def retrieve_data():
    logger.info(f"Retrieving data associated with uuid '{uuid}'...")

    try:
        stored_data = data_store.get(uuid)
    except KeyError:
        logger.warning(f"Cannot retrieve data associated with uuid '{uuid}'...")
        return jsonify({"status": "failed", "message": "data cannot be retrieved", "data": []})
            # ao invés de retornar "none", peço para retornar uma lista vazia => "[]"
            # tanto o "none" quanto a lista vazia vai significar erro
            # não é possível iterar com "none", mas é possível fazer com lista vazia
    logger.info(f"Data associated with uuid '{uuid}' retrieved successfully")
    return jsonify({"status": "failed", "message": "data retrieved successfully", "data": stored_data})

#  criação de endpoint para realizar operações em cima dos dados que estão salvos
@app.route("/data/<uuid>/<operation>", method = ["GET"])
def process.operation(uuid, operation):
    logger.info(f"Processing operation '{operation}' on data associated with UUID '{uuid}'...")

    try:
        stored_data = data_store.get(uuid)
        operation_func = get_operation(operation)
        result = operation_func(stored_data)
    except KeyError:
        logger.warning(f"Cannot retrieve data associated with uuid '{uuid}'...")
        return jsonify({"status": "failed", "message": "data cannot be retrieved", "result": None})
    except NoSuchOperationError:
        logger.warning(f"Cannot find operation '{operation}'")
        return jsonify({"status": "failed", "message": f"no such '{operation}'", "result": None})
    logger.info(f"Operation '{operation}' on data associated with UUID '{uuid}' finished successfully")
    return jsonify({"status": "success", "message": "result completed", "result": result})

class NoSuchOperationError(Exception):
    pass

def get_operation(operation_name):
    if operation_name == "min":
        return operation.op_min
    if operation_name == "max":
        return operation.op_max
    if operation_name == "mean":
        return operation.op_mean
    else:
        raise NoSuchOperationError

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)