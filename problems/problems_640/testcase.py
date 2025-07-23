from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input="x+5-3+x=6+x-2", Output="x=2"))
		self.testcases.append(case(Input="x=x", Output="Infinite solutions"))
		self.testcases.append(case(Input="2x=x", Output="x=0"))
		self.testcases.append(case(Input="0x=0", Output="Infinite solutions"))
		self.testcases.append(case(Input="-x=-1", Output="x=1"))

	def get_testcases(self):
		return self.testcases
