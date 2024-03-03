""" Main file for red passowrd and save it if it's safe """
import string
import logging
from requests import get
from hashlib import sha1

logging.basicConfig(level=logging.INFO, filename="log.log", filemode="w",
                    format="%(asctime)s - %(levelname)s - %(message)s")

logger = logging.getLogger(__name__)
handler = logging.FileHandler("logs.log")
formatter = logging.Formatter(
    "%(asctime)s - %(name)s - %(levelname)s - %(message)s")
handler.setFormatter(formatter)
logger.addHandler(handler)

logger.info("\nStart of Script\n")


class Password:
    """ Class for pasword checking and saving """

    def __init__(self) -> None:
        logger.info("Initalize Password Class")
        self.user_input_passwords = []
        self.safe_pass = []
        self.hased_words = []
        self.password_list_readed = []
        self.number_of_powned_dict = {}

    def get_user_input(self) -> str:
        """ Allows get user input savce in obj
        Returns:
            str: save user passwords in list in obj
        """
        while True:
            try:
                logging.info("Geting user input")
                user_input = input("Pleas enter you'r passwords: ").split(' ')
                self.user_input_passwords.extend(user_input)
                break
            except ValueError as error:
                logger.warning("Wrong input by user: "+error)
                print(f"Wrong input: {
                      error}\n Pleas after sentence enter space")

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
                logger.info("Password Pass all condiotion added to safe")

        if self.safe_pass == []:
            logger.warning("No save password pass , returns false")
            print("Non of your password is safe enught!")
            return False

    def hashe_words(self) -> hash:
        """ Hashed words in obj safe words
        Returns:
            hash: hashed words
        """
        logger.info("Started hased sentence")
        haseble_list = []
        for word in self.safe_pass:
            h_word = sha1(word.encode("utf-8"))
            haseble_list.append(h_word.hexdigest().upper())

        self.hased_words.extend(haseble_list)
        logger.info("finished hashed")

    def read_file_paswords(self, path="passwords.txt") -> list:
        """ Read file with passwod from txt file
        Args:
            path (str, optional): path to file. Defaults to "passwords.txt".
        Returns:
            list: extend obj passwod_list_readed
        """
        with open(path, mode="r", encoding="utf-8") as file:
            passwords_list = file.readlines()
            logger.info("Password readed from file")

        return self.password_list_readed.extend(passwords_list)

    def save_safe_passwords(self, path: str):
        """ Saves passwod in file
        Args:
            passwords (list): lit with passwods
            path (str): path to file were save
        """
        with open(path, mode="a", encoding="utf-8") as file:
            for pas in self.hased_words:
                file.writelines(pas+'\n')
                logger.info("File save")

    def pwned_checkt_count(self, url: str) -> int:
        """ Check is pasword been powned in "have i been ponwed site"
        Args:
            url (str): url - adres to api
        Returns:
            int: number of powned password save in obj
        """
        count_of_powned = 0
        dickt_powned = {}

        logger.info("Started check for powned password")
        for digit in self.hased_words:
            count_of_powned = 0

            response = get(url+digit[:5])

            if response == 400:
                dickt_powned[digit] = 0
                logger.info("Password dons't powned")

            for iterate, data in enumerate(response.text.split()):
                count_of_powned += int(data[-1])

            dickt_powned[digit] = count_of_powned

        self.number_of_powned_dict = dickt_powned

    def show_number_powned(self):
        print(f"Your password been powned: {self.number_of_powned_dict[self.hased_words[0]]} times")


if __name__ == "__main__":

    url = "https://api.pwnedpasswords.com/range/"

    my_pass = Password()
    my_pass.get_user_input()
    my_pass.check_passwords_strength()
    my_pass.hashe_words()
    my_pass.pwned_checkt_count(url)
    my_pass.show_number_powned()
    my_pass.save_safe_passwords("safe_pass.txt")
