from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[1, 3, 2, 5, 3, None, 9], Output=4))
		self.testcases.append(case(Input=[1, 3, 2, 5, None, None, 9, 6, None, 7], Output=7))
		self.testcases.append(case(Input=[1, 3, 2, 5], Output=2))
		self.testcases.append(case(Input=[0,0,0,None,0,0,None,None,0,0,None,None,0,0,None,None,0,0,None,None,0,0,None,None,0,0,None,None,0,0,None,None,0,0,None,None,0,0,None,None,0,0,None,None,0,0,None,None,0,0,None,None,0,0,None,None,0,0,None,None,0,0,None,None,0,0,None,None,0,0,None,None,0,0,None,None,0,0,None,None,0,0,None,None,0,0,None,None,0,0,None,None,0,0,None,None,0,0,None,None,0,0,None,None,0,0,None,None,0,0,None,None,0,0,None,None,0,0,None,None,0,0,None,None,0,0,None,None,0,0,None,None,0,0,None,None,0,0,None,None,0,0,None,None,0,0,None,None,0,0,None,None,0,0,None,None,0,0,None,None,0,0,None,None,0,0,None,None,0,0,None,None,0,0,None,None,0,0,None,None,0,0,None,None,0,0,None,None,0,0,None,None,0,0,None,None,0,0,None,None,0,0,None,None,0,0,None,None,0,0,None,None,0,0,None,None,0,0,None,None,0,0,None,None,0,0,None,None,0,0,None,None,0,0,None,None,0,0,None,None,0,0,None,None,0,0,None,None,0,0,None,None,0,0,None,None,0,0,None,None,0,0,None,None,0,0,None,None,0,0,None], Output=2))

	def get_testcases(self):
		return self.testcases
