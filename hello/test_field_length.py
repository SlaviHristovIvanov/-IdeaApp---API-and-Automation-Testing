import pytest

# Data for testing field length limits
field_data = [
    ('short', True),       # Valid field length
    ('thisisaverylonginputthatexceedsthelimit', False),  # Exceeds field length limit
    ('exactlyeight', True), # Exactly the field length limit
]

@pytest.mark.parametrize('input_value, expected_result', field_data)
def test_field_length(input_value, expected_result):
    max_length = 12
    if len(input_value) <= max_length:
        assert expected_result == True
    else:
        assert expected_result == False
