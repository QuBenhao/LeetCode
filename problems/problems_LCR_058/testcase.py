from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[['MyCalendar', 'book', 'book', 'book'], [[], [10, 20], [15, 25], [20, 30]]], Output=[None, True, False, True]))

	def get_testcases(self):
		return self.testcases
