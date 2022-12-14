<<<<<<< HEAD
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
=======
import random
import string


def codificar(mensagem):
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
    return mensagem_cifrada, key


def decodificar(mensagemcif,chave):
    decode = []
    for i in range(len(chave)):
        if chave[i] == '1':
            decode.append(mensagemcif[i])

    return(decode)



print('Oque você quer?\n1.Cifrar \n2.Decifrar')

resp = input()
sair = False


while sair == False:
    if resp == '1' or resp == 'Cifrar':
        print('Digite sua mensagem')
        mensagem = str(input().replace(' ',''))
        msgc,chave = codificar(mensagem)
        print(f'mensagem cifrada: {"".join(msgc).upper()}')
        print(f'chave: {"".join(chave)}')
        sair = True
    elif resp == '2' or resp == 'Decifrar':
        mensagem_c = input('digite a mensagem\n')
        key = input('digite a chave\n')
        msg_d = decodificar(mensagem_c,key)
        print(''.join(msg_d))
        sair = True   
    else:
        print('Digite 1 ou 2')
        resp = input()

print('done')
>>>>>>> be0c9e3 (Grille commit)
