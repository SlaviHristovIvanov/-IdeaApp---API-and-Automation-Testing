import pytest

login_data = [
    ("slavi123", "slavi123", True),  #correct username and correct password
    ("slavi123", "slavi124", False), #correct username and incorrect password
    ("slavi2", "slavi123", False),   #incorrect username and correct password
    ("kokolo", "gshqj1b", False),    #non-existing username and non-existing password
    (" ", " ", False)                #empty field for username and empty field for password
]

@pytest.mark.parametrize("username, password, expected_result", login_data)

def test_login(username, password, expected_result):
    if username == "slavi123" and password == "slavi123":
        assert expected_result == True
    else:
        assert expected_result == False