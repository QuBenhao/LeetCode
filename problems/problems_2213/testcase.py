from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=['babacc', 'bcb', [1, 3, 3]], Output=[3, 3, 4]))
		self.testcases.append(case(Input=['abyzz', 'aa', [2, 1]], Output=[2, 3]))

	def get_testcases(self):
		return self.testcases
