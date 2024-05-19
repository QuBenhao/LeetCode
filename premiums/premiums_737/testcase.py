from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[['great', 'acting', 'skills'], ['fine', 'drama', 'talent'], [['great', 'good'], ['fine', 'good'], ['drama', 'acting'], ['skills', 'talent']]], Output=True))
		self.testcases.append(case(Input=[['I', 'love', 'leetcode'], ['I', 'love', 'onepiece'], [['manga', 'onepiece'], ['platform', 'anime'], ['leetcode', 'platform'], ['anime', 'manga']]], Output=True))
		self.testcases.append(case(Input=[['I', 'love', 'leetcode'], ['I', 'love', 'onepiece'], [['manga', 'hunterXhunter'], ['platform', 'anime'], ['leetcode', 'platform'], ['anime', 'manga']]], Output=False))

	def get_testcases(self):
		return self.testcases
