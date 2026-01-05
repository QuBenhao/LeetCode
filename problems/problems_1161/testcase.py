from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[1, 7, 0, 7, -8, None, None], Output=2))
		self.testcases.append(case(Input=[989, None, 10250, 98693, -89388, None, None, None, -32127], Output=2))

	def get_testcases(self):
		return self.testcases
