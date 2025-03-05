import pytest


session_data = [
    (10, False),
    (30, False),
    (40, False),
    (59, False),
    (120, True)
]

@pytest.mark.parametrize('inactive_duration, expected_result', session_data)
def test_session_expiry(inactive_duration, expected_result):
    session_timeout = 60
    if inactive_duration >= session_timeout:
        assert expected_result == True
    else:
        assert expected_result == False
