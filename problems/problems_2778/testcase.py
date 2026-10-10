from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[1, 2, 3, 4], Output=21))
		self.testcases.append(case(Input=[2, 7, 1, 19, 18, 3], Output=63))

	def get_testcases(self):
		return self.testcases
