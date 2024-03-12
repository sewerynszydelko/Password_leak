"""Password leaked main script"""
from password_validator.validators import PasswordValidator, ValidationError
import sys


def password_check(path_to_save="safe_pass.txt", path_to_read="passwords.txt") -> None:
    """ Check password by validators from password file , and if it pass save into safe file
    Args:
        path_to_save (str, optional): path to file to save safe password. Defaults to "safe_pass.txt".
        path_to_read (str, optional): path to file to read pasword to check. Defaults to "passwords.txt".
    """

    with open(path_to_save, mode="a", encoding="utf-8") as file_to_save, open(path_to_read, mode="r", encoding="utf-8") as file_to_read:

        for passowrd in file_to_read:
            password_striped = passowrd.strip()
            validator = PasswordValidator(password_striped)

            try:
                validator.is_valid()
                file_to_save.write(password_striped+"\n")
                print("Pasword has been save")
            except ValidationError as error:
                print(error, " : ", password_striped)


def about() -> None:
    print("Welcom in password safty script!")
    print("In this program i will check if you'r password pass all validations")
    print("If you password pass i will save in same directory in a file 'safe_pass/txt'")
    print("Password that you given to me i will read from 'passwords.txt' placed in same directory as script file")


def get_user_choice():
    while True:
        try:
            user_input = int(input("If you want to exit just type '0'\nor any other number to contiune: "))
            if user_input == 0:
                sys.exit
            break
        except ValidationError:
            print("You give me non of numbers , pleas do so")


if __name__ == "__main__":
    about()
    get_user_choice()
    password_check()
