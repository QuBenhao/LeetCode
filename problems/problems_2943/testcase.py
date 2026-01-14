from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[2, 1, [2, 3], [2]], Output=4))
		self.testcases.append(case(Input=[1, 1, [2], [2]], Output=4))
		self.testcases.append(case(Input=[2, 3, [2, 3], [2, 4]], Output=4))
		self.testcases.append(case(Input=[1,1000000000,[2],[1000000001]], Output=4))
		self.testcases.append(case(Input=[4,40,[5,3,2,4],[36,41,6,34,33]], Output=9))

	def get_testcases(self):
		return self.testcases
