from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=['foobar', 'o'], Output=33))
		self.testcases.append(case(Input=['jjjj', 'k'], Output=0))

	def get_testcases(self):
		return self.testcases
