from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=['wrt', 'wrf', 'er', 'ett', 'rftt'], Output="wertf"))
		self.testcases.append(case(Input=['z', 'x'], Output="zx"))
		self.testcases.append(case(Input=['z', 'x', 'z'], Output=""))
		self.testcases.append(case(Input=["z","z"], Output="z"))
		self.testcases.append(case(Input=["ab","adc"], Output="abcd"))
		self.testcases.append(case(Input=["abc","ab"], Output="abc"))
		self.testcases.append(case(Input=["z","z"], Output="z"))

	def get_testcases(self):
		return self.testcases
