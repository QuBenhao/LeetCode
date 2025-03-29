from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=['LeetcodeHelpsMeLearn', [8, 13, 15]], Output="Leetcode Helps Me Learn"))
		self.testcases.append(case(Input=['icodeinpython', [1, 5, 7, 9]], Output="i code in py thon"))
		self.testcases.append(case(Input=['spacing', [0, 1, 2, 3, 4, 5, 6]], Output=" s p a c i n g"))

	def get_testcases(self):
		return self.testcases
