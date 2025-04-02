from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[12, 6, 1, 2, 7], Output=77))
		self.testcases.append(case(Input=[1, 10, 3, 4, 19], Output=133))
		self.testcases.append(case(Input=[1, 2, 3], Output=0))

	def get_testcases(self):
		return self.testcases
