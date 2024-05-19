from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[[34, 23, 1, 24, 75, 33, 54, 8], 60], Output=58))
		self.testcases.append(case(Input=[[10, 20, 30], 15], Output=-1))

	def get_testcases(self):
		return self.testcases
