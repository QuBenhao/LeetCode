from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[[[2, 2], [-1, -2], [-4, 4], [-3, 1], [3, -3]], 'abdca'], Output=2))
		self.testcases.append(case(Input=[[[1, 1], [-2, -2], [-2, 2]], 'abb'], Output=1))
		self.testcases.append(case(Input=[[[1, 1], [-1, -1], [2, -2]], 'ccd'], Output=0))

	def get_testcases(self):
		return self.testcases
