""" Test check password file """
from scripts.password import read_file_paswords, Password

test_path = "Path to your file test"
test_obj = Password()
test_obj.user_input_passwords = ["Example1!", "example1"]


def test_read_file_is_list():
    test_list = read_file_paswords(test_path)

    assert type(test_list) is list


def test_check_password_list():

    test_obj.check_passwords_strength()

    assert test_obj.safe_pass == ["Example1!"]


def test_hase_words():

    test_obj.hashe_words()

    assert type(test_obj.hased_words) == list

    test_obj.user_input_passwords = ["Example2", "Example2"]
    test_obj.hashe_words()

    assert test_obj.hased_words[0] == test_obj.hased_words[1]
