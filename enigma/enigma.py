import sys
from typing import List

# Definição dos rotores históricos da Enigma
ROTORES = {
    1: "EKMFLGDQVZNTOWYHXUSPAIBRCJ",
    2: "AJDKSIRUXBLHWTMCQGZNPYFVOE",
    3: "BDFHJLCPRTXVZNYEIWGAKMUSQO",
    4: "ESOVPZJAYQUIRHXLNFTGKDCMWB",
    5: "VZBRGITYUPSDNHLXAWMJQOFECK",
}

# Refletor fixo da Enigma
REFLETOR = "YRUHQSLDPXNGOKMIEBFZCWVJAT"

# Função para configurar os rotores
class Rotor:
    def __init__(self, wiring: str, position: int):
        self.wiring = wiring
        self.position = position - 1  # Ajuste para índice 0
        self.reverse_wiring = ''.join(sorted(wiring, key=wiring.index))

    def forward(self, char: str) -> str:
        index = (ord(char) - ord('A') + self.position) % 26
        return self.wiring[index]

    def backward(self, char: str) -> str:
        index = (self.wiring.index(char) - self.position) % 26
        return chr(index + ord('A'))

    def rotate(self) -> bool:
        self.position = (self.position + 1) % 26
        return self.position == 0

# Função principal da Enigma
class Enigma:
    def __init__(self, rotor_selection: List[int], rotor_positions: List[int]):
        self.rotors = [Rotor(ROTORES[i], pos) for i, pos in zip(rotor_selection, rotor_positions)]

    def encrypt(self, text: str) -> str:
        result = []
        for char in text:
            if not char.isalpha():
                continue
            char = char.upper()
            
            # Rotação dos rotores
            rotate_next = True
            for rotor in self.rotors:
                if rotate_next:
                    rotate_next = rotor.rotate()
                else:
                    break
            
            # Passando pelos rotores na ordem direta
            for rotor in self.rotors:
                char = rotor.forward(char)
            
            # Passando pelo refletor
            char = REFLETOR[ord(char) - ord('A')]
            
            # Passando pelos rotores na ordem inversa
            for rotor in reversed(self.rotors):
                char = rotor.backward(char)
            
            result.append(char)
        
        return ''.join(result)

# Leitura dos parâmetros
if __name__ == "__main__":
    rotores_escolhidos = list(map(int, input("Escolha 3 rotores (1-5): ").split(' ')))
    posicoes_iniciais = list(map(int, input("Escolha 3 posições iniciais (1-26): ").split(' ')))
    
    with open("mensagem.txt", "r", encoding="utf-8") as f:
        mensagem = f.read().replace("\n", "").replace(" ", "")
    
    enigma = Enigma(rotores_escolhidos, posicoes_iniciais)
    texto_cifrado = enigma.encrypt(mensagem)
    
    print("Texto cifrado:", texto_cifrado)