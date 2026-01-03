from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[21, 4, 7], Output=32))
		self.testcases.append(case(Input=[21, 21], Output=64))
		self.testcases.append(case(Input=[1, 2, 3, 4, 5], Output=0))
		self.testcases.append(case(Input=[1,2,3,4,5,6,7,8,9,10], Output=45))
		self.testcases.append(case(Input=[7286,18704,70773,8224,91675], Output=10932))

	def get_testcases(self):
		return self.testcases
