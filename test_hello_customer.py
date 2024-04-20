import unittest
from hello_customer import coffee_greeting

class TestCofeeOutput(unittest.TestCase):
    def test_output(self):
        self.assertEqual(coffee_greeting(), "Moccachino test completed")

if __name__ == "__main__":
    unittest.main()
