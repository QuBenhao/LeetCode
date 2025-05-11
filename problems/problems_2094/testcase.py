from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[2, 1, 3, 0], Output=[102, 120, 130, 132, 210, 230, 302, 310, 312, 320]))
		self.testcases.append(case(Input=[2, 2, 8, 8, 2], Output=[222, 228, 282, 288, 822, 828, 882]))
		self.testcases.append(case(Input=[3, 7, 5], Output=[]))

	def get_testcases(self):
		return self.testcases
