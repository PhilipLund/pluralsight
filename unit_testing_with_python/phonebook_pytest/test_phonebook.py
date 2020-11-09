from phone_book import PhoneBook
import pytest

def test_lookup_by_name():
    phonebook = PhoneBook()
    phonebook.add("Bob", "1234")
    assert "1234" == phonebook.lookup("Bob")

def test_phonebook_contain_all_names():
    phonebook = PhoneBook()
    phonebook.add("Bob", "1234")
    assert phonebook.names() == {"Bob"}

def test_missing_name_raises_error():
    phonebook = PhoneBook()
    with pytest.raises(KeyError):
        phonebook.lookup("Bob")
        #  phonebook.add("Bob", "1234")