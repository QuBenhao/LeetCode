from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[['Trie', 'insert', 'search', 'search', 'startsWith', 'insert', 'search'], [[], ['apple'], ['apple'], ['app'], ['app'], ['app'], ['app']]], Output=[None, None, True, False, True, None, True]))

	def get_testcases(self):
		return self.testcases
