from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[1, 3, 2, 4], Output=1))
		self.testcases.append(case(Input=[100, 1, 10], Output=9))
		self.testcases.append(case(Input=[84,11,100,100,75], Output=0))

	def get_testcases(self):
		return self.testcases
