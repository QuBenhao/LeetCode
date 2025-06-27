from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[0, 1, 2, 4, 5, 7], Output=['0->2', '4->5', '7']))
		self.testcases.append(case(Input=[0, 2, 3, 4, 6, 8, 9], Output=['0', '2->4', '6', '8->9']))
		self.testcases.append(case(Input=[-1], Output=["-1"]))

	def get_testcases(self):
		return self.testcases
