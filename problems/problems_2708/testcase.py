from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[3, -1, -5, 2, 5, -9], Output=1350))
		self.testcases.append(case(Input=[-4, -5, -4], Output=20))

	def get_testcases(self):
		return self.testcases
