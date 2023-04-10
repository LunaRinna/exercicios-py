import unittest   

from happy_birthday import func_is_birthday, isBirthday

test_value = '01.11.2022'

class TestBirthday(unittest.TestCase):
    def test_birthday(self):
        print("\nTesting whether it is someone's birthday...")
        self.assertTrue(func_is_birthday(test_value), isBirthday)

if __name__ == "__main__":
    unittest.main()