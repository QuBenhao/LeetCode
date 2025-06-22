from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[2, 5], Output=25))
		self.testcases.append(case(Input=[3, 7], Output=499))
		self.testcases.append(case(Input=[7, 17], Output=20379000))

	def get_testcases(self):
		return self.testcases
