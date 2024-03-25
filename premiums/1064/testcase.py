from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[-10, -5, 0, 3, 7], Output=3))
		self.testcases.append(case(Input=[0, 2, 5, 8, 17], Output=0))
		self.testcases.append(case(Input=[-10, -5, 3, 4, 7, 9], Output=-1))

	def get_testcases(self):
		return self.testcases
