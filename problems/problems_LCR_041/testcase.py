from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[['MovingAverage', 'next', 'next', 'next', 'next'], [[3], [1], [10], [3], [5]]], Output=[None, 1.0, 5.5, 4.66667, 6.0]))

	def get_testcases(self):
		return self.testcases
