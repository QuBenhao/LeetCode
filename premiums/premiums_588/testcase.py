from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[['FileSystem', 'ls', 'mkdir', 'addContentToFile', 'ls', 'readContentFromFile'], [[], ['/'], ['/a/b/c'], ['/a/b/c/d', 'hello'], ['/'], ['/a/b/c/d']]], Output=[None, [], None, None, ['a'], 'hello']))

	def get_testcases(self):
		return self.testcases
