from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input="A man, a plan, a canal: Panama", Output=True))
		self.testcases.append(case(Input="race a car", Output=False))

	def get_testcases(self):
		return self.testcases
