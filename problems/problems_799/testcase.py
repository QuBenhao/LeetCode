from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[1, 1, 1], Output=0.0))
		self.testcases.append(case(Input=[2, 1, 1], Output=0.5))
		self.testcases.append(case(Input=[100000009, 33, 17], Output=1.0))
		self.testcases.append(case(Input=[8, 3, 1], Output=0.87500))
		self.testcases.append(case(Input=[13, 4, 1], Output=0.87500))
		self.testcases.append(case(Input=[14, 5, 1], Output=0.03125))
		self.testcases.append(case(Input=[19, 5, 1], Output=0.62500))
		self.testcases.append(case(Input=[21, 5, 1], Output=0.87500))
		self.testcases.append(case(Input=[22, 6, 1], Output=0.0))
		self.testcases.append(case(Input=[25,6,1], Output=0.18750))

	def get_testcases(self):
		return self.testcases
