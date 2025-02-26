from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[['TextEditor', 'addText', 'deleteText', 'addText', 'cursorRight', 'cursorLeft', 'deleteText', 'cursorLeft', 'cursorRight'], [[], ['leetcode'], [4], ['practice'], [3], [8], [10], [2], [6]]], Output=[None, None, 4, None, 'etpractice', 'leet', 4, '', 'practi']))

	def get_testcases(self):
		return self.testcases
