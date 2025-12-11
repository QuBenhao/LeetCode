from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[2, [['MESSAGE', '10', 'id1 id0'], ['OFFLINE', '11', '0'], ['MESSAGE', '71', 'HERE']]], Output=[2, 2]))
		self.testcases.append(case(Input=[2, [['MESSAGE', '10', 'id1 id0'], ['OFFLINE', '11', '0'], ['MESSAGE', '12', 'ALL']]], Output=[2, 2]))
		self.testcases.append(case(Input=[2, [['OFFLINE', '10', '0'], ['MESSAGE', '12', 'HERE']]], Output=[0, 1]))

	def get_testcases(self):
		return self.testcases
