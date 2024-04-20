import unittest
from hello_customer import coffee_greeting

class TestCofeeOutput(unittest.TestCase):
    def test_output(self):
        self.assertEqual(coffee_greeting(), "CUSTOMER HELLO!")

if __name__ == "_main_":
    unittest.main()