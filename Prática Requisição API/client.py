# Script simples de teste (não faz parte da implementação do app.py)

import requests
import argparse
from loguru import logger

# criação de método para requisitar os dados
def send(data):
    response = requests.post("http://localhost:5000/data", json={"data": data})

    # no momento em que receber a requisição, quero printar o json
    print(response.json())

# criação de método para buscar os dados
def retrieve(uuid):
    response = requests.get(f"http://localhost:5000/data/{uuid}")

def request_operation(uuid, op):
    response = requests.get(f"http://localhost:5000/data/{uuid}/{operation}")

    print(response.json())

def main():
    parse = argparse.ArgumentParser(description="Test our API")
    parse.add_argument("--send", action="store_true")
    parse.add_argument("--get", action="store_true")
    parse.add_argument("--calc", action="store_true")
    parse.add_argument("--data", dest="data", type=str)
    parse.add_argument("--uuid", dest="uuid", type=str)
    parse.add_argument("--op", dest="op", type=str)

    args = parse.parse_args()

    if args.send and args.data:
        logger.info(f"Sending data '{args.data}'")

        response = send(args.data)

        logger.info(f"Response: '{response}'")
    elif args.get and args.uuid:
        logger.info(f"Retrieving data usind UUID'{args.uuid}'")

        response = retrieve(args.uuid)

        logger.info(f"Response: '{response}'")
    elif args.calc and args.uuid and args.op:
        logger.info(f"Request operation '{args.op}' using UUID '{args.uuid}'")

        responde = request_operation(args.uuid, args.op)

        response = retrieve(args.uuid)
    else:
        logger.warning(f"No action")

if __name__ == '__main__':
    main()

