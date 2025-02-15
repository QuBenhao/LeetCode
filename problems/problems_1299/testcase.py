from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[17, 18, 5, 4, 6, 1], Output=[18, 6, 6, 6, 1, -1]))
		self.testcases.append(case(Input=[400], Output=[-1]))

	def get_testcases(self):
		return self.testcases
