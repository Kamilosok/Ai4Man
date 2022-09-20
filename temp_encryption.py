import random

#Standart rsa algorithm
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


def multiplicative_inverse(e, phi):
    d = 0
    x1 = 0
    x2 = 1
    y1 = 1
    temp_phi = phi

    while e > 0:
        temp1 = temp_phi // e
        temp2 = temp_phi - temp1 * e
        temp_phi = e
        e = temp2

        x = x2 - temp1 * x1
        y = d - temp1 * y1

        x2 = x1
        x1 = x
        d = y1
        y1 = y

    if temp_phi == 1:
        return d + phi


def generate_keypair(p, q):
    n = p * q
    phi = ((p - 1) * (q - 1))

    e = random.randrange(1, phi)

    g = gcd(e, phi)
    while g != 1:
        e = random.randrange(1, phi)
        g = gcd(e, phi)

    d = multiplicative_inverse(e, phi)

    return ((e, n), (d, n))


def encrypt(pk, plaintext):
    key, n = pk
    cipher = [(ord(char) ** key) % n for char in plaintext]
    return cipher

p = 79
q = 97

public, private = generate_keypair(p, q)

message = input("Type message: ")

encrypted_msg = encrypt(public, message)

file = open("TokenButHashedAlsoPrivateKey.txt", 'w')

#Writing private key to file
file.write(str(private[0]))
file.write('\n')
file.write(str(private[1]))
file.write('\n')

#Writing encrypted token to file
for ch in encrypted_msg:
    file.write(str(ch))
    file.write('\n')



file.close()

print(f"{encrypted_msg}")

#print(f"Decrypted Message is : {decrypt(private, encrypted_msg)}")