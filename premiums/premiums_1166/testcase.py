from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[['FileSystem', 'createPath', 'get'], [[], ['/a', 1], ['/a']]], Output=[None, True, 1]))
		self.testcases.append(case(Input=[['FileSystem', 'createPath', 'createPath', 'get', 'createPath', 'get'], [[], ['/leet', 1], ['/leet/code', 2], ['/leet/code'], ['/c/d', 1], ['/c']]], Output=[None, True, True, 2, False, -1]))

	def get_testcases(self):
		return self.testcases
