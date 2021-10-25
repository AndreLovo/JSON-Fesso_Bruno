#jogador

#jogador={
#     "nome":"Andre",
#     "time":"aviadores",
#     "vivo":"True",
#     "energia":"100",
#     "mochila":["pederneira","corda","linha","arame"],
#     "aeronaves":[{"tipo":"transporte","habilidade":80},
#                  {"tipo":"ataque","habilidade":100},
#                  {"tipo":"reconhecimento","habilidade":50}]
# }

import json

jogador_j='{"nome":"Andre","time":"aviadores","vivo":"True","energia":"100","mochila":["pederneira","corda","linha","arame"],"aeronaves":[{"tipo":"transporte","habilidade":80},{"tipo":"ataque","habilidade":100},{"tipo":"reconhecimento","habilidade":50}]}'

#Transformar JSON em formato Python (formato strings)
jogador=json.loads(jogador_j)

print(jogador)

print(jogador["mochila"])

print(jogador["nome"])

print(jogador["aeronaves"])

# Atividades:
#1) Imprimir todas as chaves {}
for c in jogador:
    print (c)

#2) Imprimir todos os itens (conjunto chave - valor)
for i in jogador.items():
    print (i)

#3) Imprimir todos os valores 
for v in jogador.values():
    print(v) 

#4) Imprimir os valores das chaves: nome do jogador e o time
print(jogador["nome"])
print(jogador["time"])


#5) Imprimir todos os ítens da mochila
for im in jogador["mochila"]:
    print(im)


#6) Imprimir as aeronaves (item)
for a in jogador["aeronaves"]:
    print(a)    

#7) Imprimir os tipos de aeronaves
for b in jogador["aeronaves"]:
    print(b["tipo"])    

#8) Imprimir todas as habilidade
for c in jogador["aeronaves"]:
    print(c["habilidade"])    

#9) Imprimir tipos e habilidade juntos
for t in jogador["aeronaves"]:
    print(t["tipo"] + " - " +  str(t["habilidade"]))    
