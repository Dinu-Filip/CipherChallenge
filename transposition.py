ALPH = "abcdefghijklmnopqrstuvwxyz"


def key_clean(key: str) -> list:
    new_key = []
    for char in key:
        if char not in new_key:
            new_key.append(char)
    return new_key


def trans_encrypt(plaintext: str, key: str, block_length: int) -> tuple[str, str]:
    plaintext = [char.upper() for char in plaintext if char.isalpha()]
    #
    # Removes duplicate letters
    #
    keyword = key_clean(key)
    #
    # Stores grid of row and columns
    #
    trans_map = []
    while len(plaintext) % len(keyword) != 0:
        plaintext.append("X")

    for i in range(0, len(plaintext), len(keyword)):
        trans_map.append(plaintext[i: i + len(keyword)])

    sorted_keyword = sorted(keyword)
    #
    # Shifts columns in trans_map with ordering of keyword
    #
    for j in range(len(trans_map)):
        current_row = trans_map[j]
        new_row = ["" for _ in range(len(keyword))]
        for k in range(len(keyword)):
            new_idx = sorted_keyword.index(keyword[k])
            #
            # Moves previous letter to new position
            #
            new_row[new_idx] = current_row[k]
        trans_map[j] = new_row
    #
    # Reads along rows
    #
    horizontal_cipher_text = ""
    horizontal_trans_map = "".join(["".join(row) for row in trans_map])

    for l in range(0, len(horizontal_trans_map), block_length):
        horizontal_cipher_text += horizontal_trans_map[l: l + block_length] + " "
    #
    # Reads down columns
    #
    vertical_cipher_text = ""
    vertical_trans_map = ""
    for m in range(3):
        for n in range(len(trans_map)):
            vertical_trans_map += trans_map[n][m]

    for o in range(0, len(vertical_trans_map), block_length):
        vertical_cipher_text += vertical_trans_map[o: o + block_length] + " "

    return horizontal_cipher_text, vertical_cipher_text


def swap_columns(l: list[tuple[int, int]], ciphertext: str) -> str:
    #
    # Ciphertext must be a string separated into segments of fixed length separated by spaces
    # L is in the form [(i1, j1), (i2, j2)....], with i1 and j1, i2 and j2.... giving the indexes in each
    # segment to be swapped
    #
    segments = [list(s) for s in ciphertext.split()]
    if len(segments) == 1:
        raise Exception("ciphertext must be split into segments of fixed length separated by spaces")
    indexes = {}
    for tu in l:
        i1, i2 = tu
        if indexes.pop(i1, None):
            raise Exception(f"Index {i1} was mentioned more than once")
        if indexes.pop(i2, None):
            raise Exception(f"Index {i2} was mentioned more than once")
        indexes[i1] = 1
        indexes[i2] = 1

    for i, segment in enumerate(segments):
        for tu in l:
            i1, i2 = tu
            temp = segment[i1]
            segment[i1] = segment[i2]
            segment[i2] = temp
        segments[i] = segment
    return "\n".join("".join(l) for l in segments)
