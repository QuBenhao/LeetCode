import solution


class Solution(solution.Solution):
    def solve(self, test_input=None):
        ops, values = test_input
        # Your MyHashMap object will be instantiated and called as such:
        obj = MyHashSet()
        ans = [None]
        for i in range(1, len(ops)):
            if ops[i] == "add":
                obj.add(values[i][0])
                ans.append(None)
            elif ops[i] == "contains":
                ans.append(obj.contains(values[i][0]))
            else:
                obj.remove(values[i][0])
                ans.append(None)
        return ans


class MyHashSet(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.hash_key = 2069
        self.arr = [None] * self.hash_key

    def hash(self, key):
        return key % self.hash_key

    def add(self, key):
        """
        :type key: int
        :rtype: None
        """
        k = self.hash(key)
        if not self.arr[k]:
            self.arr[k] = [key]
        else:
            index = self.binary_search(key)
            if index < len(self.arr[k]):
                if self.arr[k][index] == key:
                    return
                elif self.arr[k][index] < key:
                    self.arr[k].insert(index + 1, key)
                else:
                    self.arr[k].insert(index, key)
            else:
                self.arr[k].append(key)

    def remove(self, key):
        """
        :type key: int
        :rtype: None
        """
        k = self.hash(key)
        if self.arr[k]:
            index = self.binary_search(key)
            if index < len(self.arr[k]) and self.arr[k][index] == key:
                self.arr[k] = self.arr[k][:index] + self.arr[k][index+1:]

    def contains(self, key):
        """
        Returns true if this set contains the specified element
        :type key: int
        :rtype: bool
        """
        k = self.hash(key)
        if self.arr[k]:
            index = self.binary_search(key)
            if index < len(self.arr[k]) and self.arr[k][index] == key:
                return True
        return False

    def binary_search(self, key):
        k = self.hash(key)
        left, right = 0, len(self.arr[k])
        while left < right:
            mid = (left + right) // 2
            if self.arr[k][mid] == key:
                return mid
            elif self.arr[k][mid] > key:
                right = mid
            else:
                left = mid + 1
        return left


# class MyHashSet(object):
#
#     def __init__(self):
#         """
#         Initialize your data structure here.
#         """
#         # better to be a prime number, less collision
#         self.key_space = 2069
#         self.hashtable = [None] * self.key_space
#
#     def add(self, key):
#         """
#         :type key: int
#         :rtype: None
#         """
#         hash_key = key % self.key_space
#         if not self.hashtable[hash_key]:
#             self.hashtable[hash_key] = ListNode(key, None, None)
#         else:
#             front = self.hashtable[hash_key]
#             back = front.last
#             while front.key <= back.key:
#                 if key == front.key:
#                     return
#                 elif key < front.key:
#                     if front == self.hashtable[hash_key]:
#                         self.hashtable[hash_key] = ListNode(key, front.last, front)
#                         front.last = self.hashtable[hash_key]
#                     else:
#                         front.last.next = ListNode(key, front.last, front)
#                         front.last = front.last.next
#                     return
#                 else:
#                     front = front.next
#                 if key == back.key:
#                     return
#                 elif key > back.key:
#                     temp = back.next
#                     back.next = ListNode(key, back, temp)
#                     if temp:
#                         temp.last = back.next
#                     else:
#                         self.hashtable[hash_key].last = back.next
#                     return
#                 else:
#                     back = back.last
#             back.next = ListNode(key, back, front)
#             front.last = back.next
#
#     def contains(self, key):
#         """
#         Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
#         :type key: int
#         :rtype: int
#         """
#         hash_key = key % self.key_space
#         front = self.hashtable[hash_key]
#         if not front:
#             return False
#         back = front.last
#         while front.key <= back.key:
#             if key == front.key:
#                 return True
#             elif key < front.key:
#                 return False
#             else:
#                 front = front.next
#             if key == back.key:
#                 return True
#             elif key > back.key:
#                 return False
#             else:
#                 back = back.last
#         return False
#
#     def remove(self, key):
#         """
#         Removes the mapping of the specified value key if this map contains a mapping for the key
#         :type key: int
#         :rtype: None
#         """
#         hash_key = key % self.key_space
#         front = self.hashtable[hash_key]
#         if not front:
#             return -1
#         back = front.last
#         while front.key <= back.key:
#             if key == front.key:
#                 if front == self.hashtable[hash_key]:
#                     self.hashtable[hash_key] = front.next
#                 else:
#                     front.last.next = front.next
#                 if front.next:
#                     front.next.last = front.last
#                 return
#             elif key < front.key:
#                 return
#             else:
#                 front = front.next
#             if key == back.key:
#                 back.last.next = back.next
#                 if back.next:
#                     back.next.last = back.last
#                 else:
#                     self.hashtable[hash_key].last = back.last
#                 return
#             elif key > back.key:
#                 return
#             else:
#                 back = back.last
#         return
#
#
# class ListNode(object):
#     def __init__(self, key, last, next):
#         """
#         :type key: int
#         :type last: HashNode
#         :type next: HashNode
#         :rtype: None
#         """
#         self.key = key
#         if not last:
#             self.last = self
#         else:
#             self.last = last
#         self.next = next
#
