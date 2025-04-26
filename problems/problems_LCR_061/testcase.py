from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[[1, 7, 11], [2, 4, 6], 3], Output=[[1, 2], [1, 4], [1, 6]]))
		self.testcases.append(case(Input=[[1, 1, 2], [1, 2, 3], 2], Output=[[1, 1], [1, 1]]))
		self.testcases.append(case(Input=[[1, 2], [3], 3], Output=[[1, 3], [2, 3]]))
		self.testcases.append(case(Input=[[1,1,2],[1,2,3],10], Output=[[1,1],[1,1],[2,1],[1,2],[1,2],[2,2],[1,3],[1,3],[2,3]]))
		self.testcases.append(case(Input=[[1,1,2],[1,2,3],10], Output=[[1,1],[1,1],[2,1],[1,2],[1,2],[2,2],[1,3],[1,3],[2,3]]))

	def get_testcases(self):
		return self.testcases
