from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[['http://news.yahoo.com', 'http://news.yahoo.com/news', 'http://news.yahoo.com/news/topics/', 'http://news.google.com', 'http://news.yahoo.com/us'], [[2, 0], [2, 1], [3, 2], [3, 1], [0, 4]], 'http://news.yahoo.com/news/topics/'], Output=['http://news.yahoo.com', 'http://news.yahoo.com/news', 'http://news.yahoo.com/news/topics/', 'http://news.yahoo.com/us']))
		self.testcases.append(case(Input=[['http://news.yahoo.com', 'http://news.yahoo.com/news', 'http://news.yahoo.com/news/topics/', 'http://news.google.com'], [[0, 2], [2, 1], [3, 2], [3, 1], [3, 0]], 'http://news.google.com'], Output=['http://news.google.com']))

	def get_testcases(self):
		return self.testcases
