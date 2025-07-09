from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[5, 1, [1, 3], [2, 5]], Output=2))
		self.testcases.append(case(Input=[10, 1, [0, 2, 9], [1, 4, 10]], Output=6))
		self.testcases.append(case(Input=[5, 2, [0, 1, 2, 3, 4], [1, 2, 3, 4, 5]], Output=0))
		self.testcases.append(case(Input=[21,1,[7,10,16],[10,14,18]], Output=7))

	def get_testcases(self):
		return self.testcases
