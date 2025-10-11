from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[5, 5, [1, 10, 100, 10000, 1000000]], Output=991600007))
		self.testcases.append(case(Input=[2, 2, [5, 4, 3, 2, 1]], Output=170))
		self.testcases.append(case(Input=[1, 1, [28]], Output=28))

	def get_testcases(self):
		return self.testcases
