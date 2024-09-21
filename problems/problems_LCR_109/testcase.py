from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[['0201', '0101', '0102', '1212', '2002'], '0202'], Output=6))
		self.testcases.append(case(Input=[['8888'], '0009'], Output=1))
		self.testcases.append(case(Input=[['8887', '8889', '8878', '8898', '8788', '8988', '7888', '9888'], '8888'], Output=-1))

	def get_testcases(self):
		return self.testcases
