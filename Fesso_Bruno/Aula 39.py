# Aula 39 - JSON em PYTHON - Parte 4 

import json

#C:/Users/André Lovo/OneDrive/Área de Trabalho/JSON/Fesso_Bruno/
with open('C:/Users/André Lovo/OneDrive/Área de Trabalho/JSON/Fesso_Bruno/jogador.json') as f:
    jogador=json.load(f)

def linha():
    print("--------------------------------------------------------------")


print(jogador)
linha()

print(jogador["mochila"])
linha()

print(jogador["nome"])
linha()

print(jogador["aeronaves"])
linha()

# Atividades:
#1) Imprimir todas as chaves {}
for c in jogador:
    print (c)
linha()

#2) Imprimir todos os itens (conjunto chave - valor)
for i in jogador.items():
    print (i)
linha()

#3) Imprimir todos os valores 
for v in jogador.values():
    print(v) 
linha()    

#4) Imprimir os valores das chaves: nome do jogador e o time
print(jogador["nome"])
linha()
print(jogador["time"])
linha()

#5) Imprimir todos os ítens da mochila
for im in jogador["mochila"]:
    print(im)
linha()

#6) Imprimir as aeronaves (item)
for a in jogador["aeronaves"]:
    print(a)    
linha()

#7) Imprimir os tipos de aeronaves
for b in jogador["aeronaves"]:
    print(b["tipo"])    
linha()

#8) Imprimir todas as habilidade
for c in jogador["aeronaves"]:
    print(c["habilidade"])    
linha()

#9) Imprimir tipos e habilidade juntos
for t in jogador["aeronaves"]:
    print(t["tipo"] + " - " +  str(t["habilidade"]))    
