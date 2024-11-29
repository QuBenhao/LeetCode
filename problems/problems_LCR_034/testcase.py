from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[['hello', 'leetcode'], 'hlabcdefgijkmnopqrstuvwxyz'], Output=True))
		self.testcases.append(case(Input=[['word', 'world', 'row'], 'worldabcefghijkmnpqstuvxyz'], Output=False))
		self.testcases.append(case(Input=[['apple', 'app'], 'abcdefghijklmnopqrstuvwxyz'], Output=False))

	def get_testcases(self):
		return self.testcases
