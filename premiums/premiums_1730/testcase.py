from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[['X', 'X', 'X', 'X', 'X', 'X'], ['X', '*', 'O', 'O', 'O', 'X'], ['X', 'O', 'O', '#', 'O', 'X'], ['X', 'X', 'X', 'X', 'X', 'X']], Output=3))
		self.testcases.append(case(Input=[['X', 'X', 'X', 'X', 'X'], ['X', '*', 'X', 'O', 'X'], ['X', 'O', 'X', '#', 'X'], ['X', 'X', 'X', 'X', 'X']], Output=-1))
		self.testcases.append(case(Input=[['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'], ['X', '*', 'O', 'X', 'O', '#', 'O', 'X'], ['X', 'O', 'O', 'X', 'O', 'O', 'X', 'X'], ['X', 'O', 'O', 'O', 'O', '#', 'O', 'X'], ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X']], Output=6))

	def get_testcases(self):
		return self.testcases
