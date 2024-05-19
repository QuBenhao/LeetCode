from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=['like', 'god', 'internal', 'me', 'internet', 'interval', 'intension', 'face', 'intrusion'], Output=['l2e', 'god', 'internal', 'me', 'i6t', 'interval', 'inte4n', 'f2e', 'intr4n']))
		self.testcases.append(case(Input=['aa', 'aaa'], Output=['aa', 'aaa']))

	def get_testcases(self):
		return self.testcases
