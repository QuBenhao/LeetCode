from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[['FileSharing', 'join', 'join', 'join', 'request', 'request', 'leave', 'request', 'leave', 'join'], [[4], [[1, 2]], [[2, 3]], [[4]], [1, 3], [2, 2], [1], [2, 1], [2], [[]]]], Output=[None, 1, 2, 3, [2], [1, 2], None, [], None, 1]))

	def get_testcases(self):
		return self.testcases
