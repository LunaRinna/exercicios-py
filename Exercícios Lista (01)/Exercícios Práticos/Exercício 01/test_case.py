import unittest   

from kilometers_to_miles import func_kilometers_to_miles

test_value = 1

class TestMiles(unittest.TestCase):
    def test_miles(self):
        print("Testing whether 1km is equal to 1.61mi...")
        self.assertEqual(func_kilometers_to_miles(test_value), 1.61)

if __name__ == "__main__":
    unittest.main()
