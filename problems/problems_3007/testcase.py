from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[9, 1], Output=6))
		self.testcases.append(case(Input=[7, 2], Output=9))
		self.testcases.append(case(Input=[3278539330613,5], Output=851568447023))

	def get_testcases(self):
		return self.testcases
