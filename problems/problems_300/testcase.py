from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[10, 9, 2, 5, 3, 7, 101, 18], Output=4))
		self.testcases.append(case(Input=[0, 1, 0, 3, 2, 3], Output=4))
		self.testcases.append(case(Input=[7, 7, 7, 7, 7, 7, 7], Output=1))

	def get_testcases(self):
		return self.testcases
