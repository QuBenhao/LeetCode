from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input="[4, 2, 6, 3, 1, 5]", Output=[4, 2, 6, 3, 1, 5]))
		self.testcases.append(case(Input="[4, 2, 6, 3, 1, 5, 7]", Output=[4, 2, 6, 3, 1, 5, 7]))
		self.testcases.append(case(Input="[-4, 2, 6, 3, 1, 5, 7]", Output=[-4, 2, 6, 3, 1, 5, 7]))

	def get_testcases(self):
		return self.testcases
