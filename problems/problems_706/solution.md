# [Python] Three approaches: doubly linked lists, insertion-sorted arrays, and balanced binary search trees

> Author: Benhao
> Date: 2021-03-08
> Upvotes: 1
> Tags: Python

---

### Approach
Linked lists make insertion and deletion easy. Sorting each list by key also makes it easier to find whether a key exists and where it belongs.

Sorted arrays support binary search.

Organizing keys in a BST allows fast lookup, but deletion takes more work, including rebalancing. An AVL Tree version is included below.

### Code

## Doubly linked list

```python
class MyHashMap(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        # better to be a prime number, less collision
        self.key_space = 2069
        self.hashtable = [None] * self.key_space

    def put(self, key, value):
        """
        value will always be non-negative.
        :type key: int
        :type value: int
        :rtype: None
        """
        hash_key = key % self.key_space
        if not self.hashtable[hash_key]:
            self.hashtable[hash_key] = ListNode(key, value, None, None)
        else:
            front = self.hashtable[hash_key]
            back = front.last
            while front.key <= back.key:
                if key == front.key:
                    front.val = value
                    return
                elif key < front.key:
                    if front == self.hashtable[hash_key]:
                        self.hashtable[hash_key] = ListNode(key, value, front.last, front)
                        front.last = self.hashtable[hash_key]
                    else:
                        front.last.next = ListNode(key, value, front.last, front)
                        front.last = front.last.next
                    return
                else:
                    front = front.next
                if key == back.key:
                    back.val = value
                    return
                elif key > back.key:
                    temp = back.next
                    back.next = ListNode(key, value, back, temp)
                    if temp:
                        temp.last = back.next
                    else:
                        self.hashtable[hash_key].last = back.next
                    return
                else:
                    back = back.last
            back.next = ListNode(key, value, back, front)
            front.last = back.next

    def get(self, key):
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        :type key: int
        :rtype: int
        """
        hash_key = key % self.key_space
        front = self.hashtable[hash_key]
        if not front:
            return -1
        back = front.last
        while front.key <= back.key:
            if key == front.key:
                return front.val
            elif key < front.key:
                return -1
            else:
                front = front.next
            if key == back.key:
                return back.val
            elif key > back.key:
                return -1
            else:
                back = back.last
        return -1

    def remove(self, key):
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        :type key: int
        :rtype: None
        """

        hash_key = key % self.key_space
        front = self.hashtable[hash_key]
        if not front:
            return -1
        back = front.last
        while front.key <= back.key:
            if key == front.key:
                if front == self.hashtable[hash_key]:
                    self.hashtable[hash_key] = front.next
                else:
                    front.last.next = front.next
                if front.next:
                    front.next.last = front.last
                return
            elif key < front.key:
                return
            else:
                front = front.next
            if key == back.key:
                back.last.next = back.next
                if back.next:
                    back.next.last = back.last
                else:
                    self.hashtable[hash_key].last = back.last
                return
            elif key > back.key:
                return
            else:
                back = back.last
        return


class ListNode(object):
    def __init__(self, key, val, last, next):
        """
        :type key: int
        :type val: int
        :type last: HashNode
        :type next: HashNode
        :rtype: None
        """
        self.key = key
        self.val = val
        if not last:
            self.last = self
        else:
            self.last = last
        self.next = next

```

## Binary search

```
class MyHashMap(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.hash_key = 2069
        self.arr = [0] * self.hash_key

    def put(self, key, value):
        """
        value will always be non-negative.
        :type key: int
        :type value: int
        :rtype: None
        """
        k = key % self.hash_key
        if not self.arr[k]:
            self.arr[k] = [[key, value]]
        else:
            index = self.binary_search(k, key)
            if index < len(self.arr[k]):
                if self.arr[k][index][0] == key:
                    self.arr[k][index][1] = value
                elif self.arr[k][index][0] < key:
                    self.arr[k].insert(index+1,[key,value])
                elif self.arr[k][index][0] > key:
                    self.arr[k].insert(index, [key,value])
            else:
                self.arr[k].append([key,value])

    def get(self, key):
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        :type key: int
        :rtype: int
        """
        k = key % self.hash_key
        if self.arr[k]:
            index = self.binary_search(k, key)
            if index < len(self.arr[k]) and self.arr[k][index][0] == key:
                return self.arr[k][index][1]
        return -1


    def remove(self, key):
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        :type key: int
        :rtype: None
        """
        k = key % self.hash_key
        if self.arr[k]:
            index = self.binary_search(k,key)
            if index < len(self.arr[k]) and self.arr[k][index][0] == key:
                self.arr[k] = self.arr[k][:index] + self.arr[k][index+1:]
    
    def binary_search(self, k, key):
        left, right = 0, len(self.arr[k])
        while left < right:
            mid = (left + right) // 2
            if self.arr[k][mid][0] == key:
                return mid
            elif self.arr[k][mid][0] > key:
                right = mid
            else:
                left = mid + 1
        return left
```

## HashTable + AVL Tree

```python
class MyHashMap(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.hash_key = 2069
        self.hash_table = [None] * self.hash_key

    def put(self, key, value):
        """
        value will always be non-negative.
        :type key: int
        :type value: int
        :rtype: None
        """
        k = key % self.hash_key
        if not self.hash_table[k]:
            self.hash_table[k] = BinarySearchTree()
        self.hash_table[k].put(key, value)

    def get(self, key):
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        :type key: int
        :rtype: int
        """
        k = key % self.hash_key
        if not self.hash_table[k]:
            return -1
        value = self.hash_table[k].get(key)
        return value if value is not None else -1

    def remove(self, key):
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        :type key: int
        :rtype: None
        """
        k = key % self.hash_key
        if self.hash_table[k]:
            try:
                self.hash_table[k].delete(key)
            except:
                pass


class TreeNode(object):
    # Initialize a tree node
    def __init__(self, key, val, left=None, right=None, parent=None, balanceFactor=0):
        self.key = key  # Node key: its position/index
        self.payload = val  # Payload: the value stored in the node
        self.leftChild = left  # Left child
        self.rightChild = right  # Right child
        self.parent = parent  # Parent node
        self.balanceFactor = balanceFactor  # Node balance factor

    # Check for a left child and return it if present
    def hasLeftChild(self):
        return self.leftChild

    # Check for a right child and return it if present
    def hasRightChild(self):
        return self.rightChild

    # Check whether this is a left child: a parent exists and its left child is self
    def isLeftChild(self):
        # Equivalent to (self.parent is not None) and (self.parent.leftChild == self)
        return self.parent and self.parent.leftChild == self

    # Check whether this is a right child
    def isRightChild(self):
        return self.parent and self.parent.rightChild == self

    # Check whether this is the root
    def isRoot(self):
        return not self.parent  # No parent

    # Check whether this is a leaf
    def isLeaf(self):
        return not (self.rightChild or self.leftChild)  # Neither child exists

    # Check whether any child exists
    def hasAnyChildren(self):
        return self.rightChild or self.leftChild  # A left or right child exists

    # Check whether both children exist
    def hasBothChildren(self):
        return self.rightChild and self.leftChild  # Both children exist

    # Replace node data
    def replaceNodeData(self, key, value, lc, rc):
        self.key = key  # Update the node key
        self.payload = value  # Update the payload
        self.leftChild = lc  # Update the left child
        self.rightChild = rc  # Update the right child
        if self.hasLeftChild():  # If a left child exists
            self.leftChild.parent = self  # Point the left child's parent to self
        if self.hasRightChild():  # If a right child exists
            self.rightChild.parent = self  # Point the right child's parent to self

    # Inorder traversal
    # A function containing yield is a generator function; its generator is also an iterator, without explicit __iter__() and __next__() methods. yield supplies each value when the generator is advanced.
    def __iter__(self):
        if self:  # If the current node exists
            if self.hasLeftChild():  # If the current node has a left child
                for elem in self.leftChild:  # Iterate over the keys in the left subtree
                    yield elem  # Yield one value without ending the loop; the next iteration resumes after this yield
            yield self.key  # Yield the current node's key
            if self.hasRightChild():  # If the current node has a right child
                for elem in self.rightChild:  # Iterate over the keys in the right subtree
                    yield elem

    # Splice out the successor so it can replace the node being deleted
    def spliceOut(self):
        if self.isLeaf():  # A leaf has no child to reconnect
            if self.isLeftChild():  # If the deleted node is its parent's left child
                self.parent.leftChild = None  # Clear the deleted node; no child needs reconnecting
            else:  # If the deleted node is its parent's right child
                self.parent.rightChild = None  # Clear the deleted node; no child needs reconnecting
        elif self.hasAnyChildren():  # If the deleted node has a child
            if self.hasLeftChild():  # If the deleted node has a left child
                if self.isLeftChild():  # If the deleted node is a left child
                    # Point the parent's left child to the deleted node's left child
                    self.parent.leftChild = self.leftChild
                else:  # If the deleted node is a right child
                    # Point the parent's right child to the deleted node's left child
                    self.parent.rightChild = self.leftChild
                # Point the deleted node's left child's parent to the deleted node's parent
                self.leftChild.parent = self.parent
            else:  # Without a left child, the deleted node must have a right child
                if self.isLeftChild():  # If the deleted node is a left child
                    # Point the parent's left child to the deleted node's right child
                    self.parent.leftChild = self.rightChild
                else:  # If the deleted node is a right child
                    # Point the parent's right child to the deleted node's right child
                    self.parent.rightChild = self.rightChild
                # Point the deleted node's right child's parent to the deleted node's parent
                self.rightChild.parent = self.parent

    # Find the deleted node's successor, which has at most one child
    def findSuccessor(self):
        succ = None  # Initialize the successor to None
        if self.hasRightChild():  # If the deleted node has a right child
            succ = self.rightChild.findMin()  # Use the minimum node in the right subtree as successor
        else:  # If the deleted node has no right child
            if self.parent:  # If the deleted node has a parent
                if self.isLeftChild():  # If the deleted node is its parent's left child
                    succ = self.parent  # The parent is the successor
                else:  # A right child's successor is its parent's successor, never the deleted node itself
                    self.parent.rightChild = None  # Temporarily detach this node so the recursive search cannot choose it
                    succ = self.parent.findSuccessor()  # Use the parent's successor
                    self.parent.rightChild = self  # Restore the node after finding the successor to preserve the tree structure
        return succ

    # Find the minimum node in this BST by following only left children
    def findMin(self):
        current = self  # Start at this node
        while current.hasLeftChild():  # Continue while a left child exists
            current = current.leftChild  # Move to the left child
        return current  # Return the leftmost node, the minimum in this subtree


# Binary search tree class (BST)
class BinarySearchTree(object):
    # Initialize an empty binary tree
    def __init__(self):
        self.root = None
        self.size = 0

    # Get the tree's size
    def length(self):
        return self.size

    # Support len() through __len__
    def __len__(self):
        return self.size

    # Implementing __iter__ makes an object iterable in for x in loops; this traversal is recursive
    # Recursion occurs on TreeNode instances, so TreeNode defines the traversal's __iter__
    def __iter__(self):
        return self.root.__iter__()  # Iterate from the root to traverse the binary search tree

    # Build the binary search tree
    def put(self, key, val):
        if self.root:  # If the tree already has a root
            self._put(key, val, self.root)  # Search the tree starting at its root
        else:  # If the tree has no root
            self.root = TreeNode(key, val)  # Create a TreeNode as the root
        self.size = self.size + 1  # Increase the tree's size

    # Tree search helper for put()
    def _put(self, key, val, currentNode):
        if key < currentNode.key:  # A smaller key belongs in the left subtree
            if currentNode.hasLeftChild():  # If there is a left subtree to search
                self._put(key, val, currentNode.leftChild)  # Search the left subtree recursively
            else:  # If there is no left subtree
                currentNode.leftChild = TreeNode(key, val, parent=currentNode)
                # Create a TreeNode as the current node's left child
                self.updateBalance(currentNode.leftChild)  # Update the left child's balance factor
        elif key == currentNode.key:  # If the new key equals the current key
            currentNode.payload = val  # Update the current node's payload
            self.size = self.size - 1  # Offset put()'s increment because this updates an existing node
        else:  # Search the right subtree when the new key is at least the current key
            if currentNode.hasRightChild():  # If there is a right subtree to search
                self._put(key, val, currentNode.rightChild)  # Search the right subtree recursively
            else:  # If there is no right subtree
                currentNode.rightChild = TreeNode(key, val, parent=currentNode)
                # Create a TreeNode as the current node's right child
                self.updateBalance(currentNode.rightChild)  # Update the right child's balance factor

    # Update balance factors
    def updateBalance(self, node):
        if node.balanceFactor > 1 or node.balanceFactor < -1:  # If the balance factor is outside -1, 0, 1
            self.rebalance(node)  # Rebalance this node
            return
        if node.parent is not None:  # If this node has a parent and is not the root
            if node.isLeftChild():  # If this is a left child
                node.parent.balanceFactor += 1  # Increase the parent's balance factor by 1
            elif node.isRightChild():  # If this is a right child
                node.parent.balanceFactor -= 1  # Decrease the parent's balance factor by 1
            if node.parent.balanceFactor != 0:  # If the parent's balance factor is nonzero
                self.updateBalance(node.parent)  # Update the parent's balance factor

    # Left rotation balances a right-heavy tree
    def rotateLeft(self, rotRoot):
        newRoot = rotRoot.rightChild  # Make the old root's right child the new root
        rotRoot.rightChild = newRoot.leftChild  # Move the new root's left child to the old root's right
        if newRoot.leftChild is not None:  # If the new root originally had a left child
            newRoot.leftChild.parent = rotRoot  # Point that child's parent to the old root
        newRoot.parent = rotRoot.parent  # Give the new root the old root's parent
        if rotRoot.isRoot():  # If the old root is the whole tree's root
            self.root = newRoot  # Set the tree's root to the new root
        else:  # If the old root is not the whole tree's root
            if rotRoot.isLeftChild():  # If the old root is a left child
                rotRoot.parent.leftChild = newRoot  # Point the parent's left child to the new root
            else:  # If the old root is a right child
                rotRoot.parent.rightChild = newRoot  # Point the parent's right child to the new root
        newRoot.leftChild = rotRoot  # Make the old root the new root's left child
        rotRoot.parent = newRoot  # Point the old root's parent to the new root
        rotRoot.balanceFactor = rotRoot.balanceFactor + 1 - min(newRoot.balanceFactor,0)
        # Update the old root's balance factor; factors within moved subtrees are unchanged. See the calculation above.
        newRoot.balanceFactor = newRoot.balanceFactor + 1 + max(rotRoot.balanceFactor,0)
        # Update the new root's balance factor; factors within moved subtrees are unchanged. See the calculation above.

    # Right rotation balances a left-heavy tree
    def rotateRight(self, rotRoot):
        newRoot = rotRoot.leftChild  # Make the old root's left child the new root
        rotRoot.leftChild = newRoot.rightChild  # Move the new root's right child to the old root's left
        if newRoot.rightChild is not None:  # If the new root originally had a right child
            newRoot.rightChild.parent = rotRoot  # Point that child's parent to the old root
        newRoot.parent = rotRoot.parent  # Give the new root the old root's parent
        if rotRoot.isRoot():  # If the old root is the whole tree's root
            self.root = newRoot  # Set the tree's root to the new root
        else:  # If the old root is not the whole tree's root
            if rotRoot.isLeftChild():  # If the old root is a left child
                rotRoot.parent.leftChild = newRoot  # Point the parent's left child to the new root
            else:  # If the old root is a right child
                rotRoot.parent.rightChild = newRoot  # Point the parent's right child to the new root
        newRoot.rightChild = rotRoot  # Make the old root the new root's right child
        rotRoot.parent = newRoot  # Point the old root's parent to the new root
        rotRoot.balanceFactor = rotRoot.balanceFactor - 1 - max(newRoot.balanceFactor, 0)
        # Update the old root's balance factor; factors within moved subtrees are unchanged. See the calculation above.
        newRoot.balanceFactor = newRoot.balanceFactor - 1 + min(0,rotRoot.balanceFactor)
        # Update the new root's balance factor; factors within moved subtrees are unchanged. See the calculation above.

    # Rebalance
    def rebalance(self, node):
        if node.balanceFactor < 0:  # If this node's balance factor is negative
            if node.rightChild.balanceFactor > 0:  # If the right child's balance factor is positive
                self.rotateRight(node.rightChild)  # Rotate the right child right
            self.rotateLeft(node)  # Rotate this node left
        elif node.balanceFactor > 0:  # If this node's balance factor is positive
            if node.leftChild.balanceFactor < 0:  # If the left child's balance factor is negative
                self.rotateLeft(node.leftChild)  # Rotate the left child left
            self.rotateRight(node)  # Rotate this node right

    # Support mytree[3]="red" through __setitem__; otherwise callers must use put()
    def __setitem__(self, k, v):
        self.put(k, v)

    # Get the value of the node indexed by key
    def get(self, key):
        if self.root:  # If the tree already has a root
            res = self._get(key, self.root)  # Search the tree starting at its root
            if res:  # If the node was found
                return res.payload  # Return the value stored in the node's payload
            else:  # If not found, no node has this key
                return None
        else:  # A tree without a root is empty
            return None

    # Tree search helper for get()
    def _get(self, key, currentNode):
        if not currentNode:  # Return None if the current node is absent
            return None
        elif currentNode.key == key:  # If the current node's key matches the requested key
            return currentNode  # Return the current node
        elif key < currentNode.key:  # If the requested key is smaller than the current key
            return self._get(key, currentNode.leftChild)  # Search the left subtree recursively
        else:  # If the requested key is at least the current key
            return self._get(key, currentNode.rightChild)  # Search the right subtree recursively

    # Support mytree[3] through __getitem__; otherwise callers must use get()
    def __getitem__(self, key):
        return self.get(key)

    # Support in through __contains__
    def __contains__(self, key):
        if self._get(key, self.root):
            return True
        else:
            return False

    # Delete the node indexed by key
    def delete(self, key):
        if self.size > 1:  # If the tree has more than one node
            nodeToRemove = self._get(key, self.root)  # Find the node to delete
            if nodeToRemove:  # If the node exists
                self.remove(nodeToRemove)  # Delete the node
                self.size = self.size - 1  # Decrease the tree's size by 1
            else:  # If the node does not exist
                raise KeyError('错误，键值不在树中')  # Report the error
        elif self.size == 1 and self.root.key == key:  # If the only node is the root being deleted
            self.root = None  # Clear the root
            self.size = self.size - 1  # Decrease the tree's size by 1
        else:  # A size-zero tree is empty
            raise KeyError('错误，键值不在树中')  # Report the error

    # Support del through __delitem__
    def __delitem__(self, key):
        self.delete(key)

    # Delete a node
    def remove(self, currentNode):
        if currentNode.isLeaf():  # A leaf has no children
            if currentNode == currentNode.parent.leftChild:  # If the deleted node is its parent's left child
                currentNode.parent.leftChild = None  # Clear the deleted node
            else:  # If the deleted node is its parent's right child
                currentNode.parent.rightChild = None  # Clear the deleted node
        elif currentNode.hasBothChildren():  # If the deleted node has two children
            succ = currentNode.findSuccessor()  # Find the successor to preserve the tree's ordering
            succ.spliceOut()  # Splice out the successor so it can replace the deleted node
            currentNode.key = succ.key  # Replace the deleted node's key with the successor's key
            currentNode.payload = succ.payload  # Replace the deleted node's payload with the successor's payload
        else:  # If the deleted node has exactly one child
            if currentNode.hasLeftChild():  # If the deleted node has only a left child
                if currentNode.isLeftChild():  # If the deleted node is a left child
                    # Point the deleted node's left child's parent to the deleted node's parent
                    currentNode.leftChild.parent = currentNode.parent
                    # Point the parent's left child to the deleted node's left child
                    currentNode.parent.leftChild = currentNode.leftChild
                elif currentNode.isRightChild():  # If the deleted node is a right child
                    # Point the deleted node's left child's parent to the deleted node's parent
                    currentNode.leftChild.parent = currentNode.parent
                    # Point the parent's right child to the deleted node's left child
                    currentNode.parent.rightChild = currentNode.leftChild
                else:  # Without a parent, the deleted node is the root
                    # Replace the deleted node's data with its left child's key, payload, and children
                    currentNode.replaceNodeData(currentNode.leftChild.key, currentNode.leftChild.payload,
                                                currentNode.leftChild.leftChild, currentNode.leftChild.rightChild)
            else:  # If the deleted node has only a right child
                if currentNode.isLeftChild():  # If the deleted node is a left child
                    # Point the deleted node's right child's parent to the deleted node's parent
                    currentNode.rightChild.parent = currentNode.parent
                    # Point the parent's left child to the deleted node's right child
                    currentNode.parent.leftChild = currentNode.rightChild
                elif currentNode.isRightChild():  # If the deleted node is a right child
                    # Point the deleted node's right child's parent to the deleted node's parent
                    currentNode.rightChild.parent = currentNode.parent
                    # Point the parent's right child to the deleted node's right child
                    currentNode.parent.rightChild = currentNode.rightChild
                else:  # Without a parent, the deleted node is the root
                    # Replace the deleted node's data with its right child's key, payload, and children
                    currentNode.replaceNodeData(currentNode.rightChild.key, currentNode.rightChild.payload,
                                                currentNode.rightChild.leftChild, currentNode.rightChild.rightChild)
```
