from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[[8, 6, 10, 5, 7, 9, 11], 12], Output=True))
		self.testcases.append(case(Input=[[8, 6, 10, 5, 7, 9, 11], 22], Output=False))

	def get_testcases(self):
		return self.testcases
