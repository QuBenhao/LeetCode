from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=['ADOBECODEBANC', 'ABC'], Output="BANC"))
		self.testcases.append(case(Input=['a', 'a'], Output="a"))
		self.testcases.append(case(Input=['a', 'aa'], Output=""))

	def get_testcases(self):
		return self.testcases
