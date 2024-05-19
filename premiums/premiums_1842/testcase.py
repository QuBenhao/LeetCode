from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input="2112", Output="2112"))
		self.testcases.append(case(Input="", Output=""))
		self.testcases.append(case(Input="54455445", Output="54455445"))

	def get_testcases(self):
		return self.testcases
