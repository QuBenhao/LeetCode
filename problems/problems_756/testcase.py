from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=['BCD', ['BCC', 'CDE', 'CEA', 'FFF']], Output=True))
		self.testcases.append(case(Input=['AAAA', ['AAB', 'AAC', 'BCD', 'BBE', 'DEF']], Output=False))

	def get_testcases(self):
		return self.testcases
