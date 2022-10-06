ALPH = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def affine_encode(plaintext: str, multiplier: int, shift: int) -> str:
    if check_valid_params(multiplier):
        split_txt = list(plaintext.lower())
        for i in range(len(split_txt)):
            char = split_txt[i]
            if 97 <= ord(char) <= 122:
                #
                # x -> ax + b
                #
                idx = ((ALPH.index(char.upper()) * multiplier) + shift) % 26
                split_txt[i] = ALPH[idx]
        return "".join(split_txt)
    else:
        return plaintext


def check_valid_params(multiplier: int) -> bool:
    #
    # The multiplier must be coprime to 26 according to mod 26 arithmetic
    #
    if multiplier % 2 == 0 or multiplier % 13 == 0 or multiplier % 26 == 0:
        return False
    return True


def affine_decode(ciphertext: str, multiplier: int, shift: int) -> str:
    if check_valid_params(multiplier):
        split_txt = list(ciphertext)
        for i in range(len(split_txt)):
            char = split_txt[i]
            if 65 <= ord(char) <= 90:
                idx = ALPH.index(char) - shift
                #
                # original idx must have been whole number
                #
                while idx < 0 or idx % multiplier != 0:
                    idx += 26
                idx //= multiplier
                split_txt[i] = ALPH[idx].lower()
        return "".join(split_txt)
    else:
        return ciphertext


def affine_brute_force(plaintext: str):
    #
    # Tries all 311 possible combinations
    #
    for i in range(1, 26):
        if check_valid_params(i):
            for j in range(0, 26):
                yield affine_decode(plaintext, i, j)