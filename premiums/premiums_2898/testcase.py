from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[1, 5, 3, 7, 8], Output=20))
		self.testcases.append(case(Input=[5, 6, 7, 8, 9], Output=35))

	def get_testcases(self):
		return self.testcases
