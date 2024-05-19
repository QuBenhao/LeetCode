from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[['ab', 'bc'], 'aabcd'], Output="a<b>abc</b>d"))
		self.testcases.append(case(Input=[['ab', 'cb'], 'aabcd'], Output="a<b>ab</b>cd"))

	def get_testcases(self):
		return self.testcases
