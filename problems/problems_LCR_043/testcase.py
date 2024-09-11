from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[['CBTInserter', 'insert', 'get_root'], [[[1]], [2], []]], Output=[None, 1, [1, 2]]))
		self.testcases.append(case(Input=[['CBTInserter', 'insert', 'insert', 'get_root'], [[[1, 2, 3, 4, 5, 6]], [7], [8], []]], Output=[None, 3, 4, [1, 2, 3, 4, 5, 6, 7, 8]]))

	def get_testcases(self):
		return self.testcases
