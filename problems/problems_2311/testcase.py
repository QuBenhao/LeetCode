from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=['1001010', 5], Output=5))
		self.testcases.append(case(Input=['00101001', 1], Output=6))

	def get_testcases(self):
		return self.testcases
