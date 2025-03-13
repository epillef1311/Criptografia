import random
import math
import matplotlib.pyplot as plt
from collections import Counter

texto = ('A criptografia tem origem no envio de informações sigilosas entre entidades militares e políticas. '
    'Mensagens precisavam ser criptografadas para parecerem textos aleatórios para qualquer pessoa, exceto para o destinatário pretendido. '
    'Atualmente, as técnicas clássicas de encriptação foram completamente quebradas. Elas foram comprometidas a ponto de serem encontradas apenas '
    'nas seções de enigmas de alguns jornais. Felizmente, o campo evoluiu bastante em segurança, e os algoritmos modernos dependem '
    'de análises avançadas e matemática rigorosa para garantir a proteção das informações. À medida que a segurança progrediu, '
    'a criptografia se expandiu para abranger uma gama mais ampla de objetivos, incluindo autenticação de mensagens, integridade de dados, '
    'computação segura e muito mais. A criptografia é a base da sociedade digital moderna, sendo essencial para a comunicação segura na Internet, '
    'transações financeiras e até mesmo moedas digitais. Um algoritmo de encriptação é um procedimento que converte uma mensagem de texto legível '
    'em um texto cifrado seguro. Os algoritmos modernos utilizam matemática avançada e uma ou mais chaves criptográficas. '
    'Isso torna relativamente fácil criptografar uma mensagem, mas extremamente difícil descriptografá-la sem conhecer as chaves. '
    'As técnicas de encriptação são divididas em duas categorias principais: simétricas e assimétricas, dependendo do funcionamento das chaves.')

key = 23
alfabeto = 'abcdefghijklmnopqrstuvwxyz'
alfabeto_tamanho = len(alfabeto)
letter_frequency_ptbr = {
    'a': 14.63, 'b': 1.04, 'c': 3.88, 'd': 4.99, 'e': 12.57, 'f': 1.02, 'g': 1.30, 'h': 1.28, 'i': 6.18, 'j': 0.40,
    'k': 0.02, 'l': 2.78, 'm': 4.74, 'n': 5.05, 'o': 10.73, 'p': 2.52, 'q': 1.20, 'r': 6.53, 's': 7.81, 't': 4.34, 'u': 4.63,
    'v': 1.67, 'w': 0.01, 'x': 0.21, 'y': 0.01, 'z': 0.47
}

def only_char_letters(text):
    return ''.join([char.lower() for char in text if char.isalpha()])

def cifra_deslocamento(message, key, decrypt=False):
    resultado = ''
    for char in message:
        if char not in alfabeto:
            resultado += char
            continue
        index = alfabeto.index(char.lower())
        shift = (index - key) if decrypt else (index + key)
        new_char = alfabeto[shift % alfabeto_tamanho]
        resultado += new_char.upper() if char.isupper() else new_char
    return resultado

def difference(message):
    counter = Counter(message)
    return sum([abs(counter.get(letter, 0) * 100 / len(message) - letter_frequency_ptbr[letter]) for letter in alfabeto]) / alfabeto_tamanho

def break_cipher(cipher_text):
    lowest_difference = math.inf
    encryption_key = 0
    for key in range(1, alfabeto_tamanho):
        current_plain_text = cifra_deslocamento(cipher_text, key, True)
        current_difference = difference(current_plain_text)
        if current_difference < lowest_difference:
            lowest_difference = current_difference
            encryption_key = key
    return encryption_key

cifra = cifra_deslocamento(only_char_letters(texto), key, False)
decript = cifra_deslocamento(cifra, key, True)
print(f'Chave usada para criptografia: {key}')
print(f'Chave descoberta pela análise de frequência: {break_cipher(cifra)}')