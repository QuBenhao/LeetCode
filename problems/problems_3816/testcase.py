from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input="aaccb", Output="aacb"))
		self.testcases.append(case(Input="z", Output="z"))

	def get_testcases(self):
		return self.testcases
