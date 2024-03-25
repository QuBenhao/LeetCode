from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[['AutocompleteSystem', 'input', 'input', 'input', 'input'], [[['i love you', 'island', 'iroman', 'i love leetcode'], [5, 3, 2, 2]], ['i'], [' '], ['a'], ['#']]], Output=[None, ['i love you', 'island', 'i love leetcode'], ['i love you', 'i loveleetcode'], [], []]))

	def get_testcases(self):
		return self.testcases
