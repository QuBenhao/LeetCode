from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[[[1, 2, 2], [2, 2, 3], [2, 3, 3]], ['ab', 'bb']], Output=None))
		self.testcases.append(case(Input=[[[1, 1, 2], [3, 3, 4], [6, 6, 6]], ['ab', '66']], Output=None))
		self.testcases.append(case(Input=[[[1, 2], [2, 1]], ['xx']], Output=None))

	def get_testcases(self):
		return self.testcases
