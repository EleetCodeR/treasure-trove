
from random import random, choices, randrange

# Sieve of Eratosthenes


def gen_primes():
    D = {}
    q = 2

    while True:
        if q not in D:
            yield q
            D[q * q] = [q]
        else:
            for p in D[q]:
                D.setdefault(p + q, []).append(p)
            del D[q]

        q += 1


def rand_prime():
    gen = gen_primes()
    bigPrimes = []
    for i in range(60):
        next(gen)

    for i in range(60):
        bigPrimes.append((next(gen)))

    return choices(bigPrimes, k=2)


def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

# Use Extended Euclid's Algorithm


def multiplicative_inverse(e, phi):
    d = 0
    x1 = 0
    x2 = 1
    y1 = 1
    temp_phi = phi

    while e > 0:
        temp1 = temp_phi//e
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


def encrypt(pr_k, plaintext):
    key, n = pr_k
    cipher = [(ord(char) ** key) % n for char in plaintext]
    return cipher


def decrypt(pub_k, ciphertext):
    key, n = pub_k
    # using a^b mod m
    plain = [chr((char ** key) % n) for char in ciphertext]
    # Return the array of bytes as a string
    return ''.join(plain)


def rsa():
    # num = rand_prime()
    # p = num[0]
    # q = num[1]
    p = int(input("Enter a prime number :"))
    q = int(input("Enter another prime number :"))
    print("\t\t: RSA Algorithm :\t\t\n")
    print(f"\nPrime Numbers => p:{p} \t q:{q} \n")
    n = p*q
    phi = (n-1)*(p-1)
    e = randrange(1, phi)
    g = gcd(e, phi)
    while g != 1:
        e = randrange(1, phi)
        g = gcd(e, phi)

    print(f"Totient func.(phi) ={phi} , e ={e}\n")
    d = multiplicative_inverse(e, phi)

    print("Generating public and private key . . .")
    # Return public and private keypair
    # Public key is (e, n) and private key is (d, n)
    return ((e, n), (d, n))


if __name__ == '__main__':
    public, private = rsa()
    print(f"\nPublic Key:{public}  , Private Key:{private}\n")
    message = input("\nEnter a message to encrypt with your private key:")
    encrypted_msg = encrypt(private, message)
    print("\nEncrypted message: ")
    print(''.join(map(lambda x: str(x), encrypted_msg)))
    print("Decrypting Message...")
    print(
        f"\n Public Key: {public} , Decrypted message:{decrypt(public, encrypted_msg)}")
