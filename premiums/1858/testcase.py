from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=['k', 'ki', 'kir', 'kira', 'kiran'], Output="kiran"))
		self.testcases.append(case(Input=['a', 'banana', 'app', 'appl', 'ap', 'apply', 'apple'], Output="apple"))
		self.testcases.append(case(Input=['abc', 'bc', 'ab', 'qwe'], Output=""))

	def get_testcases(self):
		return self.testcases
