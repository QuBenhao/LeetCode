from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[3, [[0, 1], [1, 2]], 'aac', ['query 0 2', 'update 1 b', 'query 0 2']], Output=[True, False]))
		self.testcases.append(case(Input=[4, [[0, 1], [0, 2], [0, 3]], 'abca', ['query 1 2', 'update 0 b', 'query 2 3', 'update 3 a', 'query 1 3']], Output=[False, False, True]))

	def get_testcases(self):
		return self.testcases
