""" Main file for red passowrd and save it if it's safe """
import string
from requests import get
from hashlib import sha1


def hashe_words(password_list: list[str]) -> hash:
    haseble_list = []
    for word in password_list:
        h_word = sha1(word.encode("utf-8"))
        haseble_list.append(h_word.hexdigest())

    return haseble_list
    # TODO Make Class Pasword_cahnge
    ...


def read_file_paswords(path="passwords.txt") -> list:
    with open(path, mode="r", encoding="utf-8") as file:
        passwords_list = file.readlines()

    return passwords_list


def check_passwords_strength(passwords: list[str]) -> list[bool]:

    safe_pass = []

    for password in passwords:

        list_of_conditions = [False, False, False, False, False]

        if len(password) >= 8:
            list_of_conditions[0] = True

            if any(digit.isdigit() for digit in password):
                list_of_conditions[1] = True

                if any(leter.islower() for leter in password):
                    list_of_conditions[2] = True

                    if any(leter.isupper() for leter in password):
                        list_of_conditions[3] = True

                        if any(leter in string.punctuation for leter in password):
                            list_of_conditions[4] = True

        else:
            return False

        if all(list_of_conditions):
            safe_pass.append(password)

    return safe_pass


def save_safe_passwords(passwords: list, path: str):
    with open(path, mode="a", encoding="utf-8") as file:
        for pas in passwords:
            file.writelines(pas+'\n')
