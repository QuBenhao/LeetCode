from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input="6777133339", Output="777"))
		self.testcases.append(case(Input="2300019", Output="000"))
		self.testcases.append(case(Input="42352338", Output=""))

	def get_testcases(self):
		return self.testcases
