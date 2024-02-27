""" Main file for red passowrd and save it if it's safe """
import string
from requests import get
from hashlib import sha1


class Password:

    def __init__(self) -> None:
        self.user_input_passwords = []
        self.safe_pass = []

    def get_user_input(self) -> str:
        while True:
            try:
                user_input = input("Pleas enter you'r passwords: ").split(' ')
                self.user_input_passwords.extend(user_input)
                break
            except ValueError as error:
                print(f"Wrong input: {error}\n Pleas after sentence enter space")


    def check_passwords_strength(self) -> list[str]:

        for password in self.user_input_passwords:

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

            if all(list_of_conditions):
                self.safe_pass.append(password)

    def hashe_words(self: list[str]) -> hash:
        haseble_list = []
        for word in self.safe_pass:
            h_word = sha1(word.encode("utf-8"))
            haseble_list.append(h_word.hexdigest())

        return haseble_list


def read_file_paswords(path="passwords.txt") -> list:
    with open(path, mode="r", encoding="utf-8") as file:
        passwords_list = file.readlines()

    return passwords_list


def save_safe_passwords(passwords: list, path: str):
    with open(path, mode="a", encoding="utf-8") as file:
        for pas in passwords:
            file.writelines(pas+'\n')

my_pass = Password()

my_pass.get_user_input()
my_pass.check_passwords_strength()
print(my_pass.user_input_passwords)
print(my_pass.safe_pass)