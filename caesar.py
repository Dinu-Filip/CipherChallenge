AlPH = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def caesar_decode(ciphertext: str, shift: int) -> str:
    split_cipher = list(ciphertext)
    for i in range(len(split_cipher)):
        char = split_cipher[i]
        #
        # Checks char in alphabet
        #
        if 65 <= ord(char) <= 90:
            #
            # Negative indexing applies
            #
            idx = (AlPH.index(char) - shift) % 26
            split_cipher[i] = AlPH[idx]
    return ''.join(split_cipher).lower()


def caesar_encode(plaintext: str, shift: int) -> str:
    split_cipher = list(plaintext)
    for i in range(len(split_cipher)):
        char = split_cipher[i]
        if 97 <= ord(char) <= 122:
            idx = (AlPH.index(char.upper()) + shift) % 26
            split_cipher[i] = AlPH[idx]
    return ''.join(split_cipher)


def brute_force_caesar(text: str):
    for count in range(1, 26):
        yield caesar_decode(text, count)