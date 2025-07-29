from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input="2-1-1", Output=[0, 2]))
		self.testcases.append(case(Input="2*3-4*5", Output=[-34, -14, -10, -10, 10]))

	def get_testcases(self):
		return self.testcases
