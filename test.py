from unittest import TestCase
from root_square_solver import rootSquareSolver

class CheckRootSquareSolver(TestCase):
  def test_check_two_roots(self):
    response = rootSquareSolver(1, -5, 6)
    
    self.assertEqual(len(response), 2)
    
  def test_check_root_value1(self):
    response = rootSquareSolver(1, -5, 6)
    
    self.assertIn(response[0], [2, 3])
    
  def test_check_root_value2(self):
    response = rootSquareSolver(1, -5, 6)
    
    self.assertIn(response[1], [2, 3])
    
  def test_check_one_roots(self):
    response = rootSquareSolver(1, -4, 4)
    
    self.assertEqual(len(response), 1)