from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input="YYNY", Output=2))
		self.testcases.append(case(Input="NNNNN", Output=0))
		self.testcases.append(case(Input="YYYY", Output=4))

	def get_testcases(self):
		return self.testcases
