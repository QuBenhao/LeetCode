from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[3, 3, 3, 3, 5, 5, 5, 2, 2, 7], Output=2))
		self.testcases.append(case(Input=[7, 7, 7, 7, 7, 7], Output=1))

	def get_testcases(self):
		return self.testcases
