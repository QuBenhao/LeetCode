from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[[['a', 'b'], ['b', 'c'], ['a', 'c']], [3, 0.5, 1.5]], Output=False))
		self.testcases.append(case(Input=[[['le', 'et'], ['le', 'code'], ['code', 'et']], [2, 5, 0.5]], Output=True))

	def get_testcases(self):
		return self.testcases
