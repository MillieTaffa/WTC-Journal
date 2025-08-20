import pytest
from twttr import shorten

def main():
    test_twttr()

def test_twttr():
    assert shorten("Twitter") == "Twttr"
    assert shorten("Red") == "Rd"
    assert shorten("What's your name?") == "Wht's yr nm?"
    assert shorten("CS50P") == "CS50P"
    assert shorten("123") == "123"
if __name__ == "__main__":
    main()
