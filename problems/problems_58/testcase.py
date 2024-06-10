from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input="Hello World", Output=5))
		self.testcases.append(case(Input="   fly me   to   the moon  ", Output=4))
		self.testcases.append(case(Input="luffy is still joyboy", Output=6))

	def get_testcases(self):
		return self.testcases
