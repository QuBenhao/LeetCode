from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[3, 1], Output=[-1, -1]))
		self.testcases.append(case(Input=[5, 3, 1, 2, 5, 1, 2], Output=[1, 3]))
		self.testcases.append(case(Input=[1, 3, 2, 2, 3, 2, 2, 2, 7], Output=[3, 3]))

	def get_testcases(self):
		return self.testcases
