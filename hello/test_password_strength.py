import pytest

password_data = [
    ('123456', False),          # Too weak
    ('Str0ng Passw0rd', True),  # With space
    ('password123', False),
    ('P@ssword', True)          # Special character is fine
]


@pytest.mark.parametrize('password, expected_result', password_data)
def test_password_strength(password, expected_result):
    import re
    # Updated regex to allow spaces in the password
    password_regex = r'^(?=.*[A-Za-z])(?=.*[@$!%*?&\s])[A-Za-z\d@$!%*?&\s]{8,}$'
    if re.match(password_regex, password):
        assert expected_result == True
    else:
        assert expected_result == False
