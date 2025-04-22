from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[['hello', 'leetcode'], 'hlabcdefgijkmnopqrstuvwxyz'], Output=True))
		self.testcases.append(case(Input=[['word', 'world', 'row'], 'worldabcefghijkmnpqstuvxyz'], Output=False))
		self.testcases.append(case(Input=[['apple', 'app'], 'abcdefghijklmnopqrstuvwxyz'], Output=False))
		self.testcases.append(case(Input=[["kuvp","q"],"ngxlkthsjuoqcpavbfdermiywz"], Output=True))

	def get_testcases(self):
		return self.testcases
