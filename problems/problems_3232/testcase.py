from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[1, 2, 3, 4, 10], Output=False))
		self.testcases.append(case(Input=[1, 2, 3, 4, 5, 14], Output=True))
		self.testcases.append(case(Input=[5, 5, 5, 25], Output=True))

	def get_testcases(self):
		return self.testcases
