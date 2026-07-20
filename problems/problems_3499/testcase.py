from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input="01", Output=1))
		self.testcases.append(case(Input="0100", Output=4))
		self.testcases.append(case(Input="1000100", Output=7))
		self.testcases.append(case(Input="01010", Output=4))

	def get_testcases(self):
		return self.testcases
