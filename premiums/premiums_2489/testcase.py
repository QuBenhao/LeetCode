from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=['0110011', 1, 2], Output=4))
		self.testcases.append(case(Input=['10101', 3, 1], Output=0))

	def get_testcases(self):
		return self.testcases
