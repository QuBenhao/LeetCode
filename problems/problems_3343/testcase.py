from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input="123", Output=2))
		self.testcases.append(case(Input="112", Output=1))
		self.testcases.append(case(Input="12345", Output=0))

	def get_testcases(self):
		return self.testcases
