from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[[-4, -2, 2, 4], 1, 3, 5], Output=[3, 9, 15, 33]))
		self.testcases.append(case(Input=[[-4, -2, 2, 4], -1, 3, 5], Output=[-23, -5, 1, 7]))

	def get_testcases(self):
		return self.testcases
