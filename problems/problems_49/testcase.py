from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=['eat', 'tea', 'tan', 'ate', 'nat', 'bat'], Output=[['bat'], ['nat', 'tan'], ['ate', 'eat', 'tea']]))
		self.testcases.append(case(Input=[''], Output=[['']]))
		self.testcases.append(case(Input=['a'], Output=[['a']]))

	def get_testcases(self):
		return self.testcases
