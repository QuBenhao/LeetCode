from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[['Router', 'addPacket', 'addPacket', 'addPacket', 'addPacket', 'addPacket', 'forwardPacket', 'addPacket', 'getCount'], [[3], [1, 4, 90], [2, 5, 90], [1, 4, 90], [3, 5, 95], [4, 5, 105], [], [5, 2, 110], [5, 100, 110]]], Output=[None, True, True, False, True, True, [2, 5, 90], True, 1]))
		self.testcases.append(case(Input=[['Router', 'addPacket', 'forwardPacket', 'forwardPacket'], [[2], [7, 4, 90], [], []]], Output=[None, True, [7, 4, 90], []]))

	def get_testcases(self):
		return self.testcases
