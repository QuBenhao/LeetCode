from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input="101", Output=1))
		self.testcases.append(case(Input="100", Output=2))
		self.testcases.append(case(Input="0111", Output=0))

	def get_testcases(self):
		return self.testcases
