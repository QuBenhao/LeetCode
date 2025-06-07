from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input="aaba*", Output="aab"))
		self.testcases.append(case(Input="abc", Output="abc"))
		self.testcases.append(case(Input="ee**", Output=""))

	def get_testcases(self):
		return self.testcases
