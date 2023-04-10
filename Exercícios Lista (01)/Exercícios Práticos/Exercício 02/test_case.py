import unittest   

from even_or_odd import func_is_int, func_even_or_odd

test_value = 1.6
test_value_is_odd = True

class TestFunctions(unittest.TestCase):
    def test_integer(self):
        print("\nTesting whether the value is an integer...")
        self.assertTrue(func_is_int(test_value))
    def test_even_or_odd(self):
        print("\nTesting whether the value is odd or even...")
        if test_value_is_odd == True:
            print("Test value is set to ODD...")
            self.assertEqual(func_even_or_odd(test_value), "Odd")
        else:
            print("Test value is set to EVEN...")
            self.assertEqual(func_even_or_odd(test_value), "Even")

if __name__ == "__main__":
    unittest.main()