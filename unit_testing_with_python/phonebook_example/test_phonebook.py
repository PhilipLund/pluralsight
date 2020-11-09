import unittest
from phone_book import PhoneBook

class PhoneBookTest(unittest.TestCase):

    def setUp(self) -> None:
        self.phonebook = PhoneBook()

    def tearDown(self) -> None:
        pass

    def test_lookup_by_name(self):
        
        self.phonebook.add("Bob", "12345")
        number = self.phonebook.lookup("Bob")
        self.assertEqual("12345", number)

    def test_missing_name(self):
        
        with self.assertRaises(KeyError):
            self.phonebook.lookup("missing")


    def test_is_consistent_with_different_entries(self):
        self.phonebook.add("Bob", "12345")
        self.phonebook.add("Anna", "012345")
        self.assertTrue(self.phonebook.is_consistent())
    
    def test_inconsistent_with_dublicate_entries(self):
        self.phonebook.add("Bob", "12345")
        self.phonebook.add("Anna", "12345")
        self.assertFalse(self.phonebook.is_consistent())
    
    def test_inconsistent_with_dublicate_prefix(self):
        self.phonebook.add("Bob", "12345")
        self.phonebook.add("Sue", "123")
        self.assertFalse(self.phonebook.is_consistent())
        
    def test_phonebook_adds_names_and_numbers(self):
        self.add("Sue", "123343")
        self.assertIn("Sue", self.phonebook.get_names())
        self.assertIn("123343", self.phonebook.get_numbers())
