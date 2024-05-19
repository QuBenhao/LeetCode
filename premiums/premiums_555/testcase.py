from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=['abc', 'xyz'], Output="zyxcba"))
		self.testcases.append(case(Input=['abc'], Output="cba"))

	def get_testcases(self):
		return self.testcases
