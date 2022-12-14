import random
import string
mensagem = input('Digite sua mensagem ').replace(' ','')

key = []
mensagem_cifrada = []
contador = len(mensagem)
index_da_letra = 0
for i in range(len(mensagem)*2):
    if random.randint(0,1) == 1 and contador != 0 or (len(mensagem)*2) - i == contador:
        mensagem_cifrada.append(mensagem[index_da_letra])
        contador -=1
        index_da_letra += 1
        key.append('1')
    elif i != len(mensagem)*2+1:
        randomLetter = random.choice(string.ascii_letters)
        mensagem_cifrada.append(randomLetter)
        key.append('0')

print(f'mensagem cifrada: {"".join(mensagem_cifrada).upper()}')
print(f'chave: {"".join(key)}')

decode = []
for i in range(len(key)):
    if key[i] == '1':
        decode.append(mensagem_cifrada[i])

print(''.join(decode))
