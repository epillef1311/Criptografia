import random

def modular_exp(base, exp, mod):
    if base != 0 and exp > 0 and mod > 1:
        return pow(base, exp, mod)
    return None

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def modular_inverse(a, m):
    m0, x0, x1 = m, 0, 1
    if m == 1:
        return 0
    while a > 1:
        q = a // m
        a, m = m, a % m
        x0, x1 = x1 - q * x0, x0
    return x1 + m0 if x1 < 0 else x1

def generate_keypair(p, q):
    if not is_prime(p) or not is_prime(q):
        raise ValueError("Os números fornecidos devem ser primos.")
    
    n = p * q
    phi = (p - 1) * (q - 1)
    
    e = random.randrange(2, phi)
    while gcd(e, phi) != 1:
        e = random.randrange(2, phi)
    
    d = modular_inverse(e, phi)
    return (e, n), (d, n)

def encrypt(public_key, message):
    e, n = public_key
    return [modular_exp(ord(char), e, n) for char in message]

def decrypt(private_key, encrypted_message):
    d, n = private_key
    return ''.join(chr(modular_exp(char, d, n)) for char in encrypted_message)

if __name__ == "__main__":
    p = int(input("Digite um número primo p: "))
    q = int(input("Digite um número primo q: "))
    
    try:
        public_key, private_key = generate_keypair(p, q)
        message = input("Digite a mensagem a ser encriptada: ")
        encrypted_msg = encrypt(public_key, message)
        decrypted_msg = decrypt(private_key, encrypted_msg)
        
        print(f"Mensagem Cifrada: {encrypted_msg}")
        print(f"Mensagem Original: {decrypted_msg}")
    except ValueError as e:
        print(e)
