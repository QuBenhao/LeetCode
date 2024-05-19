from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[['HitCounter', 'hit', 'hit', 'hit', 'getHits', 'hit', 'getHits', 'getHits'], [[], [1], [2], [3], [4], [300], [300], [301]]], Output=[None, None, None, None, 3, None, 4, 3]))

	def get_testcases(self):
		return self.testcases
