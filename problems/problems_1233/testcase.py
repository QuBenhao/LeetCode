from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=['/a', '/a/b', '/c/d', '/c/d/e', '/c/f'], Output=['/a', '/c/d', '/c/f']))
		self.testcases.append(case(Input=['/a', '/a/b/c', '/a/b/d'], Output=['/a']))
		self.testcases.append(case(Input=['/a/b/c', '/a/b/ca', '/a/b/d'], Output=['/a/b/c', '/a/b/ca', '/a/b/d']))

	def get_testcases(self):
		return self.testcases
