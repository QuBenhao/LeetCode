from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input="00110011", Output=6))
		self.testcases.append(case(Input="10101", Output=4))
		self.testcases.append(case(Input="00100", Output=2))

	def get_testcases(self):
		return self.testcases
