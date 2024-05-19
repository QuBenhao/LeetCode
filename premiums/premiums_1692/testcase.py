from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[3, 2], Output=3))
		self.testcases.append(case(Input=[4, 2], Output=7))
		self.testcases.append(case(Input=[20, 5], Output=206085257))

	def get_testcases(self):
		return self.testcases
