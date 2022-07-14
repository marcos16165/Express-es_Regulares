import re

with open("teste.txt") as f:
    content = f.read()
       
texto = content
letras = re.split(r'\d+', texto)
print(letras)
#['n', 'v', 'e', 'p', 'c', 'a', '']
números = re.split(r'\D+', texto)
print(números)
#['', '4', '3', '5', '4', '1', '1']
