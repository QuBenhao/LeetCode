from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=['NumArray', 'sumRange', 'sumRange', 'sumRange'], Output=[[[-2, 0, 3, -5, 2, -1]], [0, 2], [2, 5], [0, 5]]))

	def get_testcases(self):
		return self.testcases
