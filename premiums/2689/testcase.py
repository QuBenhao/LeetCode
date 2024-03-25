from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[[10, 4, 'abcpoe', 'g', 'rta'], 6], Output="b"))
		self.testcases.append(case(Input=[[12, 6, 6, 'abc', 'efg', 'hij', 'klm'], 3], Output="c"))
		self.testcases.append(case(Input=[['ropetree'], 8], Output="e"))

	def get_testcases(self):
		return self.testcases
