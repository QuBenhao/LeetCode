from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[0, 1, 0, 2, 0, 3, 0, 4, 0, 5], Output=[2, 4, 6]))
		self.testcases.append(case(Input=[1, 2, 2, 3, 4], Output=[1, 2, 5]))
		self.testcases.append(case(Input=[1, 2, 3, 4, 15], Output=[]))
		self.testcases.append(case(Input=[1,0], Output=[]))

	def get_testcases(self):
		return self.testcases
