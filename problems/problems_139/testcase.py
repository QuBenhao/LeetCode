from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=['leetcode', ['leet', 'code']], Output=True))
		self.testcases.append(case(Input=['applepenapple', ['apple', 'pen']], Output=True))
		self.testcases.append(case(Input=['catsandog', ['cats', 'dog', 'sand', 'and', 'cat']], Output=False))

	def get_testcases(self):
		return self.testcases
