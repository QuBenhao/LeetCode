from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[1, 5, 2], Output=2))
		self.testcases.append(case(Input=[3, 7], Output=7))

	def get_testcases(self):
		return self.testcases
