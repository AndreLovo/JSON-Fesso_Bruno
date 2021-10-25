# JSON em PYTHON - Parte 2 - Curso de Python 37
# Python para JSON

import json 

# dictonary -> objeto json
carros_dictionary={
    "marca":"honda",
    "modelo":"HRV",
    "cor":"prata"
}

# list -> array json
carros_list=["honda","volkswagem","ford","fiat","chevrolet"]

# tupla -> array json
carros_tupla=("honda","volkswagem","ford","fiat","chevrolet")

# Convertendo em JSON
carros_jd=json.dumps(carros_dictionary)
carros_jl=json.dumps(carros_list)
carros_jt=json.dumps(carros_tupla)

print(carros_jd)
print(carros_jl)
print(carros_jt)

carros_j=json.dumps(carros_dictionary, indent=4)
print(carros_j)

# converter : em =
carros_j=json.dumps(carros_dictionary, indent=4, separators=(": ","="), sort_keys=True)
print(carros_j)