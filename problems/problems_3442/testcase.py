from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input="aaaaabbc", Output=3))
		self.testcases.append(case(Input="abcabcab", Output=1))
		self.testcases.append(case(Input="mmsmsym", Output=-1))

	def get_testcases(self):
		return self.testcases
