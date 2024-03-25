from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[['Trie', 'insert', 'insert', 'countWordsEqualTo', 'countWordsStartingWith', 'erase', 'countWordsEqualTo', 'countWordsStartingWith', 'erase', 'countWordsStartingWith'], [[], ['apple'], ['apple'], ['apple'], ['app'], ['apple'], ['apple'], ['app'], ['apple'], ['app']]], Output=[None, None, None, 2, 2, None, 1, 1, None, 0]))

	def get_testcases(self):
		return self.testcases
