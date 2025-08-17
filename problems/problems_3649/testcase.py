from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[0, 1, 2, 3], Output=2))
		self.testcases.append(case(Input=[-3, 2, -1, 4], Output=4))
		self.testcases.append(case(Input=[1, 10, 100, 1000], Output=0))

	def get_testcases(self):
		return self.testcases
