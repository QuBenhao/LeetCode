from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[2, 6, 3, 4], Output=4))
		self.testcases.append(case(Input=[2, 10, 6, 14], Output=-1))
		self.testcases.append(case(Input=[6,10,15], Output=4))

	def get_testcases(self):
		return self.testcases
