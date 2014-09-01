import unittest

from discount_calculator import calculate_discount

class DiscountCalculatorTests(unittest.TestCase):
	def testDiscountTooLarge(self):
		with self.assertRaises(ValueError):
			final_cost = calculate_discount(100, 100, 100)

	def testDiscountNegative(self):
		with self.assertRaises(ValueError):
			final_cost = calculate_discount(100, -10, 1)


if __name__ == "__main__":
    unittest.main()