from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=['255.0.0.7', 10], Output=['255.0.0.7/32', '255.0.0.8/29', '255.0.0.16/32']))
		self.testcases.append(case(Input=['117.145.102.62', 8], Output=['117.145.102.62/31', '117.145.102.64/30', '117.145.102.68/31']))

	def get_testcases(self):
		return self.testcases
