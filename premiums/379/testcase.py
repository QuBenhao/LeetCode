from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[['PhoneDirectory', 'get', 'get', 'check', 'get', 'check', 'release', 'check'], [[3], [], [], [2], [], [2], [2], [2]]], Output=[None, 0, 1, True, 2, False, None, True]))

	def get_testcases(self):
		return self.testcases
