from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[['MyCalendarThree', 'book', 'book', 'book', 'book', 'book', 'book'], [[], [10, 20], [50, 60], [10, 40], [5, 15], [5, 10], [25, 55]]], Output=[None, 1, 1, 2, 3, 3, 3]))

	def get_testcases(self):
		return self.testcases
