from cipher_analysis import IOC


def scan_vigenere(ciphertext: str, key_length) -> str:
    #
    # Removes spaces and punctuation
    #
    cleaned_cipher = [char for char in ciphertext if char.isalnum()]
    #
    # Gets all characters at length of keyword
    #
    reg_interval_cipher = [cleaned_cipher[_] for _ in range(0, len(ciphertext), key_length)]
    return IOC("".join(reg_interval_cipher))


def get_kth_chars(ciphertext: str, key_length):
    #
    # To use with caesar cipher shift
    #
    cleaned_cipher = [char for char in ciphertext if char.isalnum()]
    return [cleaned_cipher[k] for k in range(0, len(cleaned_cipher), key_length)]
