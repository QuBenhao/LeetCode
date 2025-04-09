from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[1, 6000, 4, '124'], Output=5))
		self.testcases.append(case(Input=[15, 215, 6, '10'], Output=2))
		self.testcases.append(case(Input=[1000, 2000, 4, '3000'], Output=0))

	def get_testcases(self):
		return self.testcases
