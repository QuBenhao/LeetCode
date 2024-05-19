from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[5, 10, 10, None, None, 2, 3], Output=True))
		self.testcases.append(case(Input=[1, 2, 10, None, None, 2, 20], Output=False))

	def get_testcases(self):
		return self.testcases
