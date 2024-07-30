from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input="3[a]2[bc]", Output="aaabcbc"))
		self.testcases.append(case(Input="3[a2[c]]", Output="accaccacc"))
		self.testcases.append(case(Input="2[abc]3[cd]ef", Output="abcabccdcdcdef"))

	def get_testcases(self):
		return self.testcases
