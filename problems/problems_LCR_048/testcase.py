from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[1, 2, 3, None, None, 4, 5], Output=[1, 2, 3, None, None, 4, 5]))
		self.testcases.append(case(Input=[], Output=[]))
		self.testcases.append(case(Input=[1], Output=[1]))
		self.testcases.append(case(Input=[1, 2], Output=[1, 2]))
		self.testcases.append(case(Input=[4,-7,-3,None,None,-9,-3,9,-7,-4,None,6,None,-6,-6,None,None,0,6,5,None,9,None,None,-1,-4,None,None,None,-2], Output=[4,-7,-3,None,None,-9,-3,9,-7,-4,None,6,None,-6,-6,None,None,0,6,5,None,9,None,None,-1,-4,None,None,None,-2]))

	def get_testcases(self):
		return self.testcases
