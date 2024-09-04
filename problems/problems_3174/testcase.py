from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input="abc", Output="abc"))
		self.testcases.append(case(Input="cb34", Output=""))

	def get_testcases(self):
		return self.testcases
