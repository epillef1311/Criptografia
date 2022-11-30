import random

def criptografar(mensagem):
    key_1 = random.sample(letras, k =25)
    quadrado_1 = [key_1[:5],key_1[5:10],key_1[10:15],key_1[15:20],key_1[20:25]]
    key_2 = random.sample(letras, k =25)
    quadrado_2 = [key_2[:5],key_2[5:10],key_2[10:15],key_2[15:20],key_2[20:25]]
    coordenadas = []
    for x in mensagem:
        for y in letras_padrao:
            for z in y:
                if z == x:
                    linha, coluna = letras_padrao.index(y),y.index(z)
                    coordenadas.append([linha,coluna])
    cifra_r = []
    for i in range(len(coordenadas)):
        if i %2 == 0:
            cifra_r.append(quadrado_1[coordenadas[i][0]][coordenadas[i+1][1]])
        elif i %2 != 0:
            cifra_r.append(quadrado_2[coordenadas[i][0]][coordenadas[i-1][1]])
    return cifra_r, key_1, key_2



def decriptografar(mensagem_c,key_1,key_2):
        quadrado_1 = [key_1[:5],key_1[5:10],key_1[10:15],key_1[15:20],key_1[20:25]]
        quadrado_2 = [key_2[:5],key_2[5:10],key_2[10:15],key_2[15:20],key_2[20:25]]
        cont = 0
        cord = []
        for x in mensagem_c:
            if cont %2 ==0:
                for y in quadrado_1:
                    for z in y:
                        if x == z:
                            linha, coluna = quadrado_1.index(y), y.index(z)
                            cord.append([linha,coluna])
                            cont += 1
            elif cont %2 != 0:
                for y in quadrado_2:
                    for z in y:
                        if x == z:
                            linha, coluna = quadrado_2.index(y), y.index(z)
                            cord.append([linha,coluna])
                            cont += 1
        msg_d = []
        for i in range(len(cord)):
            if i %2 == 0:
                msg_d.append(letras_padrao[cord[i][0]][cord[i+1][1]])
            elif i %2 != 0:
                msg_d.append(letras_padrao[cord[i][0]][cord[i-1][1]])
        if msg_d[-1] == 'x':
            msg_d = msg_d[:-1]
        return msg_d



letras = ['A','B','C','D','E','F','G','H','I','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
letras_padrao = [['a','b','c','d','e'],['f','g','h','i','k'],['l','m','n','o','p'],['q','r','s','t','u'],['v','w','x','y','z']]


print('Oque você quer?\n1.Cifrar \n2.Decifrar')

resp = input()
sair = False


while sair == False:
    if resp == '1' or resp == 'Cifrar':
        print('Digite sua mensagem')
        mensagem = str(input())
        mensagem.lower()
        if len(mensagem) %2 != 0:
            mensagem = mensagem + 'x'
            mensagem_cr,key_1_cr, key_2_cr = criptografar(mensagem)
            
            print(f'mensagem: {"".join(mensagem_cr)}\nChave 1: {"".join(key_1_cr)}\nchave 2: {"".join(key_2_cr)}')
            sair = True
        else:
            mensagem_cr,key_1_cr, key_2_cr = criptografar(mensagem)
            
            print(f'mensagem: {"".join(mensagem_cr)}\nChave 1: {"".join(key_1_cr)}\nchave 2: {"".join(key_2_cr)}')
            sair = True
  
    elif resp == '2' or resp == 'Decifrar':
        mensagem_c = input('digite a mensagem')
        key_1 = input('digite a primeira chave')
        key_2 = input('digite a segunda chave')
        msg_d = decriptografar(mensagem_c,key_1,key_2)
        print(''.join(msg_d))
        sair = True   
    else:
        print('Digite 1 ou 2')
        resp = input()

print('done')



