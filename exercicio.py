__author__ = "Luna Antunes"

import unittest

def add_suffix(prefix):
    suffix = ["ack", "uack"]
    match prefix:
        case "O" | "Q":
            return prefix + suffix[1]
        case _:
            return prefix + suffix[0]

class TestSuffix(unittest.TestCase):
    def testing_jack(self):
        print("Testando se J = Jack...")
        self.assertEqual(add_suffix("J"), "Jack")
    def testing_kack(self):
        print("Testando se K = Kack...")
        self.assertEqual(add_suffix("K"), "Kack")
    def testing_lack(self):
        print("Testando se L = Lack...")
        self.assertEqual(add_suffix("L"), "Lack")
    def testing_mack(self):
        print("Testando se M = Mack...")
        self.assertEqual(add_suffix("M"), "Mack")
    def testing_nack(self):
        print("Testando se N = Nack...")
        self.assertEqual(add_suffix("N"), "Nack")
    def testing_ouack(self):
        print("Testando se O = Ouack...")
        self.assertEqual(add_suffix("O"), "Ouack")
    def testing_pack(self):
        print("Testando se P = Pack...")
        self.assertEqual(add_suffix("P"), "Pack")
    def testing_quack(self):
        print("Testando se Q = Quack...")
        self.assertEqual(add_suffix("Q"), "Quack")
        
test1 = TestSuffix().testing_jack()
test2 = TestSuffix().testing_kack()
test3 = TestSuffix().testing_lack()
test4 = TestSuffix().testing_mack()
test5 = TestSuffix().testing_nack()
test6 = TestSuffix().testing_ouack()
test7 = TestSuffix().testing_pack()
test8 = TestSuffix().testing_quack()