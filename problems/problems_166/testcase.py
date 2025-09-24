from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[1, 2], Output="0.5"))
		self.testcases.append(case(Input=[2, 1], Output="2"))
		self.testcases.append(case(Input=[4, 333], Output="0.(012)"))
		self.testcases.append(case(Input=[-50,8], Output="-6.25"))

	def get_testcases(self):
		return self.testcases
