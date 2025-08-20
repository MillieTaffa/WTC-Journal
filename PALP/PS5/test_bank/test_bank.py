import pytest
from bank import value

def main():
    test_hello()
    test_startswith_h()
    test_other()

def test_hello():
    assert value("hello") == 0
    assert value("Hello, Millie") == 0

def test_startswith_h():
    assert value("hey") == 20
    assert value("Hey, Millie") == 20

def test_other():
    assert value("good morning") == 100
    assert value("Good morning, Millie") == 100

if __name__ == "__main__":
    main()


