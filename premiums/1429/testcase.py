from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[['FirstUnique', 'showFirstUnique', 'add', 'showFirstUnique', 'add', 'showFirstUnique', 'add', 'showFirstUnique'], [[[2, 3, 5]], [], [5], [], [2], [], [3], []]], Output=[None, 2, None, 2, None, 3, None, -1]))
		self.testcases.append(case(Input=[['FirstUnique', 'showFirstUnique', 'add', 'add', 'add', 'add', 'add', 'showFirstUnique'], [[[7, 7, 7, 7, 7, 7]], [], [7], [3], [3], [7], [17], []]], Output=[None, -1, None, None, None, None, None, 17]))
		self.testcases.append(case(Input=[['FirstUnique', 'showFirstUnique', 'add', 'showFirstUnique'], [[[809]], [], [809], []]], Output=[None, 809, None, -1]))

	def get_testcases(self):
		return self.testcases
