from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[['cat', 'bat', 'rat'], 'the cattle was rattled by the battery'], Output="the cat was rat by the bat"))
		self.testcases.append(case(Input=[['a', 'b', 'c'], 'aadsfasf absbs bbab cadsfafs'], Output="a a b c"))
		self.testcases.append(case(Input=[['a', 'aa', 'aaa', 'aaaa'], 'a aa a aaaa aaa aaa aaa aaaaaa bbb baba ababa'], Output="a a a a a a a a bbb baba a"))
		self.testcases.append(case(Input=[['catt', 'cat', 'bat', 'rat'], 'the cattle was rattled by the battery'], Output="the cat was rat by the bat"))
		self.testcases.append(case(Input=[['ac', 'ab'], 'it is abnormal that this solution is accepted'], Output="it is ab that this solution is ac"))

	def get_testcases(self):
		return self.testcases
