import unittest
from multiply import multiplication
class MultiplyTestCase(unittest.TestCase):

  def test_1(self):

      result = mulitplication(3,4)
  
      self.asserEqual(result,12)

def test_2(self):
  
      result = mulitplication(3,-4)
  
      self.asserEqual(result,-12)

def test_3(self):
  
      result = mulitplication(-3,-4)
  
      self.asserEqual(result,12)

   

  
