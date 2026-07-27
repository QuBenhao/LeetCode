from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input="z", Output="z"))
		self.testcases.append(case(Input="babab", Output="abbba"))
		self.testcases.append(case(Input="daccad", Output="acddca"))

	def get_testcases(self):
		return self.testcases
