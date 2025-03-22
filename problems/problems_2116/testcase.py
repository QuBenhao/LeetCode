from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=['))()))', '010100'], Output=True))
		self.testcases.append(case(Input=['()()', '0000'], Output=True))
		self.testcases.append(case(Input=[')', '0'], Output=False))
		self.testcases.append(case(Input=['(((())(((())', '111111010111'], Output=True))

	def get_testcases(self):
		return self.testcases
