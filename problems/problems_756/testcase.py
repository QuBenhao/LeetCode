from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=['BCD', ['BCC', 'CDE', 'CEA', 'FFF']], Output=True))
		self.testcases.append(case(Input=['AAAA', ['AAB', 'AAC', 'BCD', 'BBE', 'DEF']], Output=False))
		self.testcases.append(case(Input=["ABCD",["ABC","BCA","CDA","ABD","BCE","CDF","DEA","EFF","AFF"]], Output=True))

	def get_testcases(self):
		return self.testcases
