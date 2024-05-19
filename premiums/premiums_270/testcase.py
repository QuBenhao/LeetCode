from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[[4, 2, 5, 1, 3], 3.714286], Output=4))
		self.testcases.append(case(Input=[[1], 4.428571], Output=1))

	def get_testcases(self):
		return self.testcases
