""" Main file for red passowrd and save it if it's safe """
import string
from requests import get
from hashlib import sha1


class Password:
    """ Class for pasword checking and saving """

    def __init__(self) -> None:
        self.user_input_passwords = []
        self.safe_pass = []
        self.hased_words = []
        self.password_list_readed = []

    def get_user_input(self) -> str:
        """ Allows get user input savce in obj
        Returns:
            str: save user passwords in list in obj
        """
        while True:
            try:
                user_input = input("Pleas enter you'r passwords: ").split(' ')
                self.user_input_passwords.extend(user_input)
                break
            except ValueError as error:
                print(f"Wrong input: {error}\n Pleas after sentence enter space")


    def check_passwords_strength(self) -> list[str]:
        """ Check if password pass 5 levels of passwod strenght
        Returns:
            list[str]: save passwod that safle fulfils all conditions
        """

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


    def hashe_words(self) -> hash:
        """ Hashed words in obj safe words
        Returns:
            hash: hashed words
        """
        haseble_list = []
        for word in self.safe_pass:
            h_word = sha1(word.encode("utf-8"))
            haseble_list.append(h_word.hexdigest())

        self.hased_words.extend(haseble_list)


    def read_file_paswords(self,path="passwords.txt") -> list:
        """ Read file with passwod from txt file
        Args:
            path (str, optional): path to file. Defaults to "passwords.txt".
        Returns:
            list: extend obj passwod_list_readed
        """
        with open(path, mode="r", encoding="utf-8") as file:
            passwords_list = file.readlines()

        return self.password_list_readed.extend(passwords_list)


    @staticmethod
    def save_safe_passwords(passwords: list, path: str):
        """ Saves passwod in file
        Args:
            passwords (list): lit with passwods
            path (str): path to file were save
        """
        with open(path, mode="a", encoding="utf-8") as file:
            for pas in passwords:
                file.writelines(pas+'\n')


if __name__ == "__main__":
    pass