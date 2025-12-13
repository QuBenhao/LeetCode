from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input="SSPPSPS", Output=3))
		self.testcases.append(case(Input="PPSPSP", Output=1))
		self.testcases.append(case(Input="S", Output=0))

	def get_testcases(self):
		return self.testcases
