from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[1, 1, 2], Output=2))
		self.testcases.append(case(Input=[1, 2, 1], Output=1))
		self.testcases.append(case(Input=[3, 3, 2], Output=14))
		self.testcases.append(case(Input=[59,60,34], Output=182913914))
		self.testcases.append(case(Input=[200,200,100], Output=70669177))

	def get_testcases(self):
		return self.testcases
