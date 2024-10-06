from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[1, 1, []], Output=0))
		self.testcases.append(case(Input=[100, 1, [[10, 100]]], Output=-1))
		self.testcases.append(case(Input=[100, 10, [[10, 60], [20, 30], [30, 30], [60, 40]]], Output=2))

	def get_testcases(self):
		return self.testcases
