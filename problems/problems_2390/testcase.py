from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input="leet**cod*e", Output="lecoe"))
		self.testcases.append(case(Input="erase*****", Output=""))

	def get_testcases(self):
		return self.testcases
