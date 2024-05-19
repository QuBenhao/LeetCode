from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[1, 2, 3], Output=25))
		self.testcases.append(case(Input=[4, 9, 0, 5, 1], Output=1026))

	def get_testcases(self):
		return self.testcases
