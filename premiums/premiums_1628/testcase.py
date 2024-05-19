from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=['3', '4', '+', '2', '*', '7', '/'], Output=2))
		self.testcases.append(case(Input=['4', '5', '2', '7', '+', '-', '*'], Output=-16))

	def get_testcases(self):
		return self.testcases
