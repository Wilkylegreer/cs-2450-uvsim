import unittest
from math_instructions import MathInstructions
from control_instructions import ControlInstructions


class Memory:
    def __init__(self):
        self.size = 100
        self.mem = [0] * self.size

class TestMath(unittest.TestCase):
  def __init__(self):
    self.memory = Memory()
    self.math = MathInstructions(self.memory)

  def test_add_positive(self):
    self.memory.mem[33] = 2
    accumulator = 5
    accumulator = self.math.add(accumulator, 33)
    self.assertEqual(accumulator, 7)

  def test_add_zero(self):
    self.memory.mem[33] = 0
    accumulator = 5
    accumulator = self.math.add(accumulator, 33)
    self.assertEqual(accumulator, 5)

  def test_subtract(self):
    self.memory.mem[33] = 10
    accumulator = 15
    accumulator = self.math.subtract(accumulator, 33)
    self.assertEqual(accumulator, 5)

  def test_subtract_zero(self):
    self.memory.mem[33] = 0
    accumulator = 5
    accumulator = self.math.subtract(accumulator, 33)
    self.assertEqual(accumulator, 5)

  def test_divide(self):
    self.memory.mem[33] = 5
    accumulator = 10
    accumulator = self.math.divide(accumulator, 33)
    self.assertEqual(accumulator, 2)

  def test_divide_zero(self):
    self.memory.mem[33] = 0
    accumulator = 10
    with self.assertRaises(ZeroDivisionError):
      self.math.divide(accumulator, 33)

  def test_multiply(self):
    self.memory.mem[33] = 5
    accumulator = 5
    accumulator = self.math.multiply(accumulator, 33)
    self.assertEqual(accumulator, 25)

  def test_multiply_zero(self):
    self.memory.mem[33] = 0
    accumulator = 5
    accumulator = self.math.multiply(accumulator, 33)
    self.assertEqual(accumulator, 0)

if __name__ == "__main__":
    unittest.main()
