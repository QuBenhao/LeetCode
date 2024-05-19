from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=['abcxyz123', ['abc', '123']], Output="<b>abc</b>xyz<b>123</b>"))
		self.testcases.append(case(Input=['aaabbb', ['aa', 'b']], Output="<b>aaabbb</b>"))

	def get_testcases(self):
		return self.testcases
