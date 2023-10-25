import json

x = '{ "nome":"Raphael", "idade":39, "cidade":"Rio de Janeiro"}'
y = json.loads(x)
print(f"Nome: {y['nome']}, Idade: {y['idade']}")
y = json.loads(x)
print(y["cidade"])