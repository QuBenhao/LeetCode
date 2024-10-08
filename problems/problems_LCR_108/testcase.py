from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=['hit', 'cog', ['hot', 'dot', 'dog', 'lot', 'log', 'cog']], Output=5))
		self.testcases.append(case(Input=['hit', 'cog', ['hot', 'dot', 'dog', 'lot', 'log']], Output=0))

	def get_testcases(self):
		return self.testcases
