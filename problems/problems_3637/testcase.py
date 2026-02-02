from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[1, 3, 5, 4, 2, 6], Output=True))
		self.testcases.append(case(Input=[2, 1, 3], Output=False))
		self.testcases.append(case(Input=[5,9,1,7], Output=True))

	def get_testcases(self):
		return self.testcases
