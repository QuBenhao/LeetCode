from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input="['acdf', 'acef', 'bcdf', 'bcef']", Output=['acdf', 'acef', 'bcdf', 'bcef']))
		self.testcases.append(case(Input="['abcd']", Output=['abcd']))

	def get_testcases(self):
		return self.testcases
