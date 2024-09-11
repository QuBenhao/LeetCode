from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[3, 5, 2, 4], Output=2))
		self.testcases.append(case(Input=[9, 2, 5, 4], Output=4))
		self.testcases.append(case(Input=[7, 6, 8], Output=0))

	def get_testcases(self):
		return self.testcases
