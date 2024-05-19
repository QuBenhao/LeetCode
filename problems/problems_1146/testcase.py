from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[['SnapshotArray', 'set', 'snap', 'set', 'get'], [[3], [0, 5], [], [0, 6], [0, 0]]], Output=[None, None, 0, None, 5]))

	def get_testcases(self):
		return self.testcases
