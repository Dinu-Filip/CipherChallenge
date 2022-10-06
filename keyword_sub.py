ALPH = "abcdefghijklmnopqrstuvwxyz"


def create_key(keyword: str) -> list:
    key = []
    #
    # Removes duplicate letters in keyword
    # Keyword must be uppercase
    #
    for char in keyword:
        if char not in key:
            key.append(char)
    #
    # Finds next letter in alphabet after last to continue key
    #
    start_idx = (ALPH.index(key[-1].lower()) + 1) % 26
    while ALPH[start_idx].upper() in key:
        start_idx += 1
        start_idx %= 26
    #
    # Appends remaining alphabet letters
    #
    for i in range(start_idx, start_idx + 26):
        current = ALPH[i % 26].upper()
        if current not in key:
            key.append(current)
    return key


def keyword_encrypt(plaintext: str, keyword: str) -> str:
    ciphertext = [char.lower() for char in plaintext]
    encrypt_key = create_key(keyword)
    for i in range(len(plaintext)):
        current = ciphertext[i]
        #
        # Passes any characters that are not letters
        #
        if 97 <= ord(current) <= 122:
            ciphertext[i] = encrypt_key[ALPH.index(current)].upper()
    return ''.join(ciphertext)


def keyword_decrypt(ciphertext: str, keyword: str) -> str:
    plaintext = [char.lower() for char in ciphertext]
    decrypt_key = create_key(keyword)
    for i in range(len(plaintext)):
        current = plaintext[i]
        if 97 <= ord(current) <= 122:
            plaintext[i] = ALPH[decrypt_key.index(current)]
    return ''.join(plaintext)
