ALPH = "abcdefghijklmnopqrstuvwxyz"


def create_key(keyword: str) -> list:
    key = []
    #
    # Removes duplicate letters in keyword, which must be uppercase
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


def replace_letters(ciphertext: str, mappings: dict, plain_to_cipher):
    print("PRINTING KEY FROM PLAINTEXT TO CIPHERTEXT")
    mappings = {k.lower(): mappings[k].lower() for k in mappings.keys()}
    ciphertext = ciphertext.lower()
    assert len(set(mappings.values())) == len(mappings.values()) and len(set(mappings.keys())) == len(mappings.keys())
    sorted_mappings = sorted(mappings.items(), key=lambda t: t[1])
    if plain_to_cipher:
        print("\n".join(":".join(c) for c in sorted_mappings))
    else:
        print("\n".join(":".join(c[::-1]) for c in sorted_mappings))
    print("PRINTING FORMATTED CIPHERTEXT")
    output = "".join(mappings[c] if c in mappings.keys() else (f"-{c}-" if c.isalpha() else c) for c in ciphertext)
    return output


def get_nth_most_common_substrings(tuples: list[tuple], ciphertext: str):
    #
    # Takes a list of tuples in the form [(l, n)] and
    # finds the nth most common substrings of length l
    # in the ciphertext
    #
    for tu in tuples:
        l, n = tu
        occurrences = {}
        for i in range(len(ciphertext) - l):
            substring = ciphertext[i:i + l]
            occurrences[substring] = occurrences.pop(substring, 0) + 1
        most_common_substrings = sorted(occurrences.items(), key=lambda t: t[1])[-n:]
        print(f"Length: {l}")
        result = ", ".join(f"{t[0]}: {t[1]}" for t in most_common_substrings)
        print(result)
