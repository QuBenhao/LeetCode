from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[10, [3, 9, 19, 5, 21]], Output=True))
		self.testcases.append(case(Input=[5, [4, 9, 23, 4]], Output=False))

	def get_testcases(self):
		return self.testcases
