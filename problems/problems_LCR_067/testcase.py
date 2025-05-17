from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[3, 10, 5, 25, 2, 8], Output=28))
		self.testcases.append(case(Input=[0], Output=0))
		self.testcases.append(case(Input=[2, 4], Output=6))
		self.testcases.append(case(Input=[8, 10, 2], Output=10))
		self.testcases.append(case(Input=[14, 70, 53, 83, 49, 91, 36, 80, 92, 51, 66, 70], Output=127))

	def get_testcases(self):
		return self.testcases
