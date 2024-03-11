"""Password leaked main script"""
from password_validator.validators import PasswordValidator, ValidationError


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


if __name__ == "__main__":
    password_check()
