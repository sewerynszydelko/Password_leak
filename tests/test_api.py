""" Test api reuqest mock data file """
from scripts.password import Password

url = "https://api.pwnedpasswords.com/range/"

test_hashe = 'C6A0BEE6B245D41C810C29759D723563CBA29DC1'
answear = "00076EB545721DADDEF4E790A7C81ADB2D0:4"


def test_api_method(requests_mock):
    """ test if given hashe func count right count
    Args:
        requests_mock (_type_): mocking request for test
    """
    # given
    test_password = Password()
    test_password.safe_pass = ["Example1!"]
    test_password.hashe_words()
    
    # when
    requests_mock.get(url+test_hashe[:5], text=answear)
    test_password.pwned_checkt_count(url)

    # then
    assert test_password.number_of_powned_dict[test_hashe] == 4
