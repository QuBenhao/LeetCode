from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input="LMCT", Output=2))
		self.testcases.append(case(Input="LCCT", Output=4))
		self.testcases.append(case(Input="L", Output=0))
		self.testcases.append(case(Input="LCTKLCLT", Output=7))

	def get_testcases(self):
		return self.testcases
