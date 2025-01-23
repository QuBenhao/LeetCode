from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[3, 1, 2], Output=4))
		self.testcases.append(case(Input=[1, 10, 1, 1], Output=2))
		self.testcases.append(case(Input=[26, 18, 6, 12, 49, 7, 45, 45], Output=39))

	def get_testcases(self):
		return self.testcases
