import unittest

def add(num1: int, num2: int) -> int:
    return num1 + num2

def mul(num1: int, num2: int) -> int:
    return num1 * num2


class TestMathOperations(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(0, 0), 0)
    
    def test_mul(self):
        self.assertEqual(mul(2, 3), 6)
        self.assertEqual(mul(-1, 1), -1)
        self.assertEqual(mul(0, 5), 0)
        self.assertNotEqual(mul(2, 4), 0)
    
    def test_assertions(self):
        self.assertTrue(3 > 2)
        self.assertFalse(3 < 2)
        self.assertIsNone(None)
        self.assertIsNotNone("hello")
        self.assertIn(3, [1, 2, 3])

if __name__ == '__main__':
    unittest.main()

    try:
        assert 3 > 2, "3 is not greater than 2"
        assert 3 < 2, "3 is not less than 2"
    except AssertionError as e:
        print(e)