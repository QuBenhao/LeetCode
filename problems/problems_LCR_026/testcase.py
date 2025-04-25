from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[1, 2, 3, 4], Output=[1, 4, 2, 3]))
		self.testcases.append(case(Input=[1, 2, 3, 4, 5], Output=[1, 5, 2, 4, 3]))
		self.testcases.append(case(Input=[1], Output=[1]))
		self.testcases.append(case(Input=[1,2,3,4,5,6,7], Output=[1,7,2,6,3,5,4]))

	def get_testcases(self):
		return self.testcases
