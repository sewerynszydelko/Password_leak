""" Test check password file """
from scripts.check_password import read_file_paswords, check_passwords_strength, save_safe_passwords

test_path = "Path to your file test"


def test_read_file_is_list():
    test_list = read_file_paswords(test_path)

    assert type(test_list) is list


def test_check_password_list():

    test_bool_list = check_passwords_strength(["Example1!", "example1"])

    assert test_bool_list == ["Example1!"]
