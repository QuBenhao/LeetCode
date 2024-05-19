from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=['abcdefghijklmnopqrstuvwxyz', 'cba'], Output=4))
		self.testcases.append(case(Input=['pqrstuvwxyzabcdefghijklmno', 'leetcode'], Output=73))

	def get_testcases(self):
		return self.testcases
