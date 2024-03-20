import solution
from object_libs import call_method


class Solution(solution.Solution):
    def solve(self, test_input=None):
        ops, inputs = test_input
        obj = Trie()
        return [None] + [call_method(obj, op, *ipt) for op, ipt in zip(ops[1:], inputs[1:])]


# class Trie(object):
#
#     def __init__(self):
#         """
#         Initialize your data structure here.
#         """
#         self.root = {}
#
#     def insert(self, word):
#         """
#         Inserts a word into the trie.
#         :type word: str
#         :rtype: None
#         """
#         node = self.root
#         for c in word:
#             if c not in node:
#                 node[c] = {}
#             node = node[c]
#         node['end'] = True
#
#     def search(self, word):
#         """
#         Returns if the word is in the trie.
#         :type word: str
#         :rtype: bool
#         """
#         node = self.root
#         for c in word:
#             if c not in node:
#                 return False
#             node = node[c]
#         return 'end' in node
#
#     def startsWith(self, prefix):
#         """
#         Returns if there is any word in the trie that starts with the given prefix.
#         :type prefix: str
#         :rtype: bool
#         """
#         node = self.root
#         for c in prefix:
#             if c not in node:
#                 return False
#             node = node[c]
#         return True


class Trie(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: None
        """
        node = self.root
        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
        node.is_word = True

    def search_prefix(self, word):
        node = self.root
        for c in word:
            if c not in node.children:
                return None
            node = node.children[c]
        return node

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        node = self.search_prefix(word)
        return node is not None and node.is_word

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        return self.search_prefix(prefix) is not None


class TrieNode(object):
    def __init__(self):
        self.children = {}
        self.is_word = False

# class Trie(object):
#     def __init__(self):
#         """
#         Initialize your data structure here.
#         """
#         self.root = TrieNode()
#
#     def insert(self, word):
#         """
#         Inserts a word into the trie.
#         :type word: str
#         :rtype: None
#         """
#         node = self.root
#         for i in range(len(word)):
#             if not node.containsKey(word[i]):
#                 node.put(word[i], TrieNode())
#             node = node.get(word[i])
#         node.isEnd = True
#
#     def searchPrefix(self, word):
#         node = self.root
#         for i in range(len(word)):
#             if node.containsKey(word[i]):
#                 node = node.get(word[i])
#             else:
#                 return None
#         return node
#
#     def search(self, word):
#         """
#         Returns if the word is in the trie.
#         :type word: str
#         :rtype: bool
#         """
#         node = self.searchPrefix(word)
#         return node is not None and node.isEnd
#
#     def startsWith(self, prefix):
#         """
#         Returns if there is any word in the trie that starts with the given prefix.
#         :type prefix: str
#         :rtype: bool
#         """
#         node = self.searchPrefix(prefix)
#         return node is not None
#
#
# class TrieNode:
#     def __init__(self):
#         self.__R = 26
#         self.isEnd = False
#         self.links = [None] * self.__R
#
#     def containsKey(self, ch):
#         return self.links[ord(ch) - ord('a')] is not None
#
#     def get(self, ch):
#         return self.links[ord(ch) - ord('a')]
#
#     def put(self, ch, node):
#         self.links[ord(ch) - ord('a')] = node
