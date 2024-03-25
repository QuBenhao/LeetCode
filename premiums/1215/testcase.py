from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[0, 21], Output=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 21]))
		self.testcases.append(case(Input=[10, 15], Output=[10, 12]))

	def get_testcases(self):
		return self.testcases
