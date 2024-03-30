from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=['abba', 'dog cat cat dog'], Output=True))
		self.testcases.append(case(Input=['abba', 'dog cat cat fish'], Output=False))
		self.testcases.append(case(Input=['aaaa', 'dog cat cat dog'], Output=False))

	def get_testcases(self):
		return self.testcases
