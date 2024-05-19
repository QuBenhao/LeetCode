from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[['StringIterator', 'next', 'next', 'next', 'next', 'next', 'next', 'hasNext', 'next', 'hasNext'], [['L1e2t1C1o1d1e1'], [], [], [], [], [], [], [], [], []]], Output=[None, 'L', 'e', 'e', 't', 'C', 'o', True, 'd', True]))

	def get_testcases(self):
		return self.testcases
