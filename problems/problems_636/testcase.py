from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[2, ['0:start:0', '1:start:2', '1:end:5', '0:end:6']], Output=[3, 4]))
		self.testcases.append(case(Input=[1, ['0:start:0', '0:start:2', '0:end:5', '0:start:6', '0:end:6', '0:end:7']], Output=[8]))
		self.testcases.append(case(Input=[2, ['0:start:0', '0:start:2', '0:end:5', '1:start:6', '1:end:6', '0:end:7']], Output=[7, 1]))

	def get_testcases(self):
		return self.testcases
