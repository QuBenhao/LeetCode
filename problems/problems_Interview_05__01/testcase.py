from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[1024, 19, 2, 6], Output=1100))
		self.testcases.append(case(Input=[0, 31, 0, 4], Output=31))
		self.testcases.append(case(Input=[1143207437,1017033,11,31], Output=2082885133))

	def get_testcases(self):
		return self.testcases
