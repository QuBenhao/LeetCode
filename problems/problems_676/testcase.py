from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[['MagicDictionary', 'buildDict', 'search', 'search', 'search', 'search'], [[], [['hello', 'leetcode']], ['hello'], ['hhllo'], ['hell'], ['leetcoded']]], Output=[None, None, False, True, False, False]))

	def get_testcases(self):
		return self.testcases
