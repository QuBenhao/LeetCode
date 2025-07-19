from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[3, 4, 5, 2], Output=12))
		self.testcases.append(case(Input=[1, 5, 4, 5], Output=16))
		self.testcases.append(case(Input=[3, 7], Output=12))

	def get_testcases(self):
		return self.testcases
