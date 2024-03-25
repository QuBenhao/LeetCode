from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[10, 3, 4, 2, 1], Output=2))
		self.testcases.append(case(Input=[2, 3, None, 2, None], Output=0))
		self.testcases.append(case(Input=[0], Output=1))

	def get_testcases(self):
		return self.testcases
