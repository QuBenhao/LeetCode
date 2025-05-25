from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input="abc", Output="a"))
		self.testcases.append(case(Input="bcda", Output=""))
		self.testcases.append(case(Input="zdce", Output="zdce"))

	def get_testcases(self):
		return self.testcases
