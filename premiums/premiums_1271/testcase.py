from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input="IOI", Output="IOI"))
		self.testcases.append(case(Input="ERROR", Output="ERROR"))

	def get_testcases(self):
		return self.testcases
