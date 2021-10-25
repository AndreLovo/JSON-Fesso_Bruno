# JSON em PYTHON - Curso de Python 36

import json

carros_json= '{"marca":"honda", "modelo": "HRV", "cor": "prata"}'

carros=json.loads(carros_json)

#print(carros)

#print(carros["marca"])

#print(carros["modelo"])

for k,v in carros.items():
    print(k + " - "+ v)

    