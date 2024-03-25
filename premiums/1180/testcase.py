from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input="8", Output=8))
		self.testcases.append(case(Input="55", Output=55))

	def get_testcases(self):
		return self.testcases
