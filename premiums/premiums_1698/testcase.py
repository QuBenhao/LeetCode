from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input="21", Output=21))
		self.testcases.append(case(Input="28", Output=28))

	def get_testcases(self):
		return self.testcases
