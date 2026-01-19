from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[2, 3, 5, 7], Output=[-1, 1, 4, 3]))
		self.testcases.append(case(Input=[11, 13, 31], Output=[9, 12, 15]))

	def get_testcases(self):
		return self.testcases
