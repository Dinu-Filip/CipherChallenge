import matplotlib.pyplot as plt
import numpy as np

ALPH = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def frequency_analysis(ciphertext: str) -> None:
    comp_list = {}
    cipher = ''.join(e for e in ciphertext if e.isalpha())
    cipher = cipher.lower()

    for char in cipher:
        if char not in comp_list:
            comp_list[char] = 1
        else:
            comp_list[char] += 1

    display_frequencies(comp_list, len(cipher))


def order_letters(freq_dict: dict) -> list:
    ordered_letters = []
    empty = True
    for letter in freq_dict.keys():
        if empty:
            ordered_letters.append(letter)
            empty = False
        else:
            for i in reversed(range(len(ordered_letters))):
                if freq_dict[ordered_letters[i]] >= freq_dict[letter]:
                    ordered_letters.insert(i + 1, letter)
                    break
                else:
                    if i == 0:
                        ordered_letters.insert(0, letter)
    return ordered_letters


def display_frequencies(freq_dict: dict, length: int):
    ordered_letters = order_letters(freq_dict)

    print("Number of individual occurences")
    for i in range(len(ordered_letters)):
        print(f"{i + 1}. {ordered_letters[i]}: {freq_dict[ordered_letters[i]]}")
    print("===============================")
    print("Percentage of individual occurences")
    for j in range(len(ordered_letters)):
        print(f"{j + 1}. {ordered_letters[j]}: {(freq_dict[ordered_letters[j]] / length) * 100}%")
    print("===============================")
    #
    # Creates graph that illustrates frequencies for easy comparison
    #
    ax_1 = plt.subplot(111)
    ax_2 = ax_1.twiny()
    x = ordered_letters
    x_axis = np.arange(26)
    y_1 = [(freq_dict[letter] / length) * 100 for letter in ordered_letters]
    y_2 = [12.02, 9.1, 8.12, 7.68, 7.31, 6.95, 6.28, 6.02, 5.92, 4.32, 3.98, 2.88, 2.71, 2.61, 2.3, 2.11, 2.09, 2.03,
           1.82, 1.49, 1.11, 0.69, 0.17, 0.11, 0.1, 0.07]

    while len(y_1) < 26:
        y_1.append(0)
    while len(x) < 26:
        x.append("-")

    ax_1.bar(x_axis - 0.2, y_2, width=0.4)
    ax_1.bar(x_axis + 0.2, y_1, width=0.4)
    ax_1.set_xticks(x_axis + 0.1, x)

    ax_2.set_xlim(ax_1.get_xlim())
    ax_2.set_xticks(ticks=range(0, 26))
    ax_2.set_xticklabels(np.array([char for char in "etaoinsrhdlucmfywgpbvkxqjz"]))
    ax_2.set_xlabel("Frequency of letters in English alphabet")
    ax_1.set_xlabel("Frequency of letters in ciphertext")
    ax_1.legend(labels=["English alphabet", "ciphertext"])
    plt.show()


def IOC(cipher: str) -> float:
    #
    # Calculates index of coincidence
    #
    total = 0
    for char in ALPH.upper():
        n_char = cipher.count(char)
        total += n_char * (n_char - 1)
    num_chars = 0
    for i in cipher:
        if 65 <= ord(i) <= 90:
            num_chars += 1
    #
    # (n(n - 1))/(N(N - 1))
    #
    return total / (num_chars * (num_chars - 1))