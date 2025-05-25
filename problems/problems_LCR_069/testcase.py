from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[0, 1, 0], Output=1))
		self.testcases.append(case(Input=[0, 2, 1, 0], Output=1))
		self.testcases.append(case(Input=[0, 10, 5, 2], Output=1))
		self.testcases.append(case(Input=[3, 4, 5, 1], Output=2))
		self.testcases.append(case(Input=[24, 69, 100, 99, 79, 78, 67, 36, 26, 19], Output=2))

	def get_testcases(self):
		return self.testcases
