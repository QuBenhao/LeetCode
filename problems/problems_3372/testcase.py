from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[[[0, 1], [0, 2], [2, 3], [2, 4]], [[0, 1], [0, 2], [0, 3], [2, 7], [1, 4], [4, 5], [4, 6]], 2], Output=[9, 7, 9, 8, 8]))
		self.testcases.append(case(Input=[[[0, 1], [0, 2], [0, 3], [0, 4]], [[0, 1], [1, 2], [2, 3]], 1], Output=[6, 3, 3, 3, 3]))
		self.testcases.append(case(Input=[[[0,1]],[[0,1]],0], Output=[1,1]))

	def get_testcases(self):
		return self.testcases
