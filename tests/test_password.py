""" Test check password file """
from scripts.password import read_file_paswords, Password

# given
test_path = "Path to your file test"
test_obj = Password()
test_obj.user_input_passwords = ["Example1!", "example1"]


def test_read_file_is_list():
    """ testing if readed file is list
    """
    # when
    test_list = read_file_paswords(test_path)

    # then
    assert type(test_list) is list


def test_check_password_list():
    """Test if func work give list
    """
    # when
    test_obj.check_passwords_strength()

    # then
    assert test_obj.safe_pass == ["Example1!"]


def test_hase_words():
    """test if hase func work on pre drfine examples
    """
    # when
    test_obj.hashe_words()

    #then
    assert type(test_obj.hased_words) == list

    test_obj.user_input_passwords = ["Example2", "Example2"]
    test_obj.hashe_words()

    assert test_obj.hased_words[0] == test_obj.hased_words[1]
