""" Test check password file """
from scripts.check_password import read_file_paswords, check_passwords_strength, save_safe_passwords, hashe_words

test_path = "Path to your file test"


def test_read_file_is_list():
    test_list = read_file_paswords(test_path)

    assert type(test_list) is list


def test_check_password_list():

    test_words_list = check_passwords_strength(["Example1!", "example1"])

    assert test_words_list == ["Example1!"]


def test_hase_words():
    test_words_list = ["Example1!", "example1"]
    test_words_same_list = ["Example2","Example2"]

    test_1_result = hashe_words(test_words_list)
    test_2_result = hashe_words(test_words_same_list)

    assert type(test_1_result) == list
    assert test_2_result[0] == test_2_result[1]