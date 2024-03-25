from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=['thestoryofleetcodeandme', ['story', 'fleet', 'leetcode']], Output=[[3, 7], [9, 13], [10, 17]]))
		self.testcases.append(case(Input=['ababa', ['aba', 'ab']], Output=[[0, 1], [0, 2], [2, 3], [2, 4]]))

	def get_testcases(self):
		return self.testcases
