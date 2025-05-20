from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[1, 2, 3, 4, 5, 6, None, None, None, 7, 8, 9, 10, None, None, 11, 12], Output=[1, 2, 3, 7, 8, 11, 12, 9, 10, 4, 5, 6]))
		self.testcases.append(case(Input=[1, 2, None, 3], Output=[1, 3, 2]))
		self.testcases.append(case(Input=[], Output=[]))
		self.testcases.append(case(Input=[1,2,3,4,5,6,None,None,None,7,8,None,None,11,12], Output=[1,2,3,7,8,11,12,4,5,6]))
		self.testcases.append(case(Input=[1,2,3,4,5,6,None,7,8,9,10,None,None,11,12], Output=[1,7,8,11,12,9,10,2,3,4,5,6]))

	def get_testcases(self):
		return self.testcases
