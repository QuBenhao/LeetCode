from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input="RR.L", Output="RR.L"))
		self.testcases.append(case(Input=".L.R...LR..L..", Output="LL.RR.LLRRLL.."))

	def get_testcases(self):
		return self.testcases
