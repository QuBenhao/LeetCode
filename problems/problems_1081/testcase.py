from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input="bcabc", Output="abc"))
		self.testcases.append(case(Input="cbacdcbc", Output="acdb"))

	def get_testcases(self):
		return self.testcases
