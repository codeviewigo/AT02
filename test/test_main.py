import pytest

from main import count_vowels


@pytest.mark.parametrize("s, expected", [
    ("aeiou", 5),
    ("AEIOU", 5),
    ("bcdfg", 0),
    ("BXHFG", 0),
    ("aEiOuBCDFG", 5),
    ("Hello, World!", 3),
    ("PyThOn", 1),
])
def test_count_vowels(s, expected):
    assert count_vowels(s) == expected


if __name__ == "__main__":
    pytest.main()
