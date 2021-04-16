import json

import re


def setup():
    print("Iniciando carregamento da lista deny.txt com CPF's inválidos")
    data = []
    f = open('deny.txt', 'r')
    lines = f.readlines()
    numbers = [n.replace('\n', '') for n in lines]
    counter = 1
    for n in numbers:
        n = re.sub("[^0-9]", '', n)

        cpf_object = {
            "model": "cpf.cpf",
            "pk": counter,
            "fields": {
                "number": n,
                "status": "DENY"
            }
        }
        data.append(cpf_object)
        counter += 1
    with open('initial_cpf_data.json', 'w') as outfile:
        json.dump(data, outfile)
    f.close()


setup()