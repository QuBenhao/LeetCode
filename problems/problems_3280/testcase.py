from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input="2080-02-29", Output="100000100000-10-11101"))
		self.testcases.append(case(Input="1900-01-01", Output="11101101100-1-1"))

	def get_testcases(self):
		return self.testcases
