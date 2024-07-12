from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[8, 4, 2, 30, 15], Output=True))
		self.testcases.append(case(Input=[1, 2, 3, 4, 5], Output=True))
		self.testcases.append(case(Input=[3, 16, 8, 4, 2], Output=False))

	def get_testcases(self):
		return self.testcases
