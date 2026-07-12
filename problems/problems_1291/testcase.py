from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[100, 300], Output=[123, 234]))
		self.testcases.append(case(Input=[1000, 13000], Output=[1234, 2345, 3456, 4567, 5678, 6789, 12345]))

	def get_testcases(self):
		return self.testcases
