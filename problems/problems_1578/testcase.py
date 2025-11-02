from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=['abaac', [1, 2, 3, 4, 5]], Output=3))
		self.testcases.append(case(Input=['abc', [1, 2, 3]], Output=0))
		self.testcases.append(case(Input=['aabaa', [1, 2, 3, 4, 1]], Output=2))

	def get_testcases(self):
		return self.testcases
