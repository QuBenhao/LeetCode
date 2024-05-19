from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input="11", Output=11))
		self.testcases.append(case(Input="12", Output=12))
		self.testcases.append(case(Input="15", Output=15))

	def get_testcases(self):
		return self.testcases
