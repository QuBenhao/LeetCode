from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[3, 2, 1, 4], Output=7))
		self.testcases.append(case(Input=[8, 6, 7, 7], Output=4))
		self.testcases.append(case(Input=[1], Output=1))
		self.testcases.append(case(Input=[12,11,10,9,8,7,6,5,4,3,4,3,10,9,8,7], Output=68))

	def get_testcases(self):
		return self.testcases
