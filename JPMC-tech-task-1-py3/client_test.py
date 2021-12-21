import unittest
from client3 import *

class ClientTest(unittest.TestCase):
  def test_getDataPoint_calculatePrice(self):
    quotes = [
      {'top_ask': {'price': 121.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """
    for quote in quotes:
      self.assertEqual(getDataPoint(quote), (quote['stock'], quote['top_bid']['price'], quote['top_ask']['price'], (quote['top_bid']['price'] + quote['top_ask']['price']) / 2))

  def test_getDataPoint_calculatePriceBidGreaterThanAsk(self):
    quotes = [
      {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """
    for quote in quotes:
      self.assertEqual(getDataPoint(quote), (quote['stock'], quote['top_bid']['price'], quote['top_ask']['price'], (quote['top_bid']['price'] + quote['top_ask']['price']) / 2))

  """ ------------ Add more unit tests ------------ """

  def test_getRatio(self): #Basic funcionality
    test_priceA = {'ABC': 68.7}
    test_priceB = {'DEF': 72.1 }
    expected_value = (68.7 / 72.1)
    self.assertEqual((getRatio((test_priceA['ABC']), (test_priceB['DEF']))), expected_value)

  def test_getRatio_divisonByZero(self): #When price B is zero
    test_priceA = 121.6
    test_priceB = 0
    expected_value = None
    self.assertEqual(getRatio(test_priceA, test_priceB), (expected_value))
      
  def test_getRatio_multiplicationByZero(self): #When price A is zero
    test_priceA = 0
    test_priceB = 121.6
    expected_value = 0
    self.assertEqual(getRatio(test_priceA, test_priceB), (expected_value)) 
    


if __name__ == '__main__':
    unittest.main()
