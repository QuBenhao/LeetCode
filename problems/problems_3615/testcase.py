from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[3, [[0, 1], [1, 2]], 'aba'], Output=3))
		self.testcases.append(case(Input=[3, [[0, 1], [0, 2]], 'abc'], Output=1))
		self.testcases.append(case(Input=[4, [[0, 2], [0, 3], [3, 1]], 'bbac'], Output=3))
		self.testcases.append(case(Input=[6,[[0,3],[4,5],[3,2],[1,4],[3,5]],"kllokm"], Output=1))

	def get_testcases(self):
		return self.testcases
