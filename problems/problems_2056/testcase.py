from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[['rook'], [[1, 1]]], Output=15))
		self.testcases.append(case(Input=[['queen'], [[1, 1]]], Output=22))
		self.testcases.append(case(Input=[['bishop'], [[4, 3]]], Output=12))

	def get_testcases(self):
		return self.testcases
