from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[['D', '.', '*'], ['.', '.', '.'], ['.', 'S', '.']], Output=3))
		self.testcases.append(case(Input=[['D', 'X', '*'], ['.', '.', '.'], ['.', '.', 'S']], Output=-1))
		self.testcases.append(case(Input=[['D', '.', '.', '.', '*', '.'], ['.', 'X', '.', 'X', '.', '.'], ['.', '.', '.', '.', 'S', '.']], Output=6))

	def get_testcases(self):
		return self.testcases
