""" Main file for red passowrd and save it if it's safe """
import string


def read_file_paswords(path="passwords.txt") -> list:
    with open(path, mode="r", encoding="utf-8") as file:
        passwords_list = file.readlines()

    return passwords_list


def check_passwords_strength(passwords: str) -> bool:

    list_of_conditions = [False, False, False, False, False]

    for password in passwords:
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

    return list_of_conditions


print(check_passwords_strength(["Placki123!"]))

"""
test = "Placki123!"
letter_list = [s for s in test]
digits_list = [d for d in string.digits]
print(letter_list)
print(digits_list)
print(any(d.isdigit() for d in test))
"""
