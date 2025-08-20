import pytest
from working import convert

def main():
    test_wrong_format()
    test_time()
    test_wrong_hour()
    test_wrong_minute()

def test_wrong_format():
    with pytest.raises(ValueError):
        convert('9 am - 5 pm')

def test_time():
    assert convert('9 am to 5 pm') == '09:00 to 17:00'
    assert convert('10 pm to 8 am') == '22:00 to 08:00'
    assert convert('10:30 pm to 8:50 am') == '22:30 to 08:50'

def test_wrong_hour():
     with pytest.raises(ValueError):
        convert('9 am to 17 pm')

def test_wrong_minute():
     with pytest.raises(ValueError):
        convert('9:60 am to 9:60 pm')
if __name__ == "__main__":
    main()
