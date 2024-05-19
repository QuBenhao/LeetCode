# 2792. Count Nodes That Are Great Enough

<p>You are given a <code>root</code> to a binary tree and an integer <code>k</code>. A node of this tree is called <strong>great enough</strong> if the followings hold:</p>

<ul>
	<li>Its subtree has <strong>at least</strong> <code>k</code> nodes.</li>
	<li>Its value is <b>greater</b> than the value of <strong>at least</strong> <code>k</code> nodes in its subtree.</li>
</ul>

<p>Return<em> the number of nodes in this tree that are great enough.</em></p>

<p>The node <code>u</code> is in the <strong>subtree</strong> of the node&nbsp;<code>v</code>, if <code><font face="monospace">u == v</font></code>&nbsp;or&nbsp;<code>v</code>&nbsp;is an&nbsp;ancestor of <code>u</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> root = [7,6,5,4,3,2,1], k = 2
<strong>Output:</strong> 3
<strong>Explanation:</strong> Number the nodes from 1 to 7.
The values in the subtree of node 1: {1,2,3,4,5,6,7}. Since node.val == 7, there are 6 nodes having a smaller value than its value. So it&#39;s great enough.
The values in the subtree of node 2: {3,4,6}. Since node.val == 6, there are 2 nodes having a smaller value than its value. So it&#39;s great enough.
The values in the subtree of node 3: {1,2,5}. Since node.val == 5, there are 2 nodes having a smaller value than its value. So it&#39;s great enough.
It can be shown that other nodes are not great enough.
See the picture below for a better understanding.</pre>

<p><img alt="" src="https://assets.leetcode.com/uploads/2023/07/25/1.png" style="padding: 10px; background: rgb(255, 255, 255); border-radius: 0.5rem; width: 300px; height: 167px;" /></p>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> root = [1,2,3], k = 1
<strong>Output:</strong> 0
<strong>Explanation: </strong>Number the nodes from 1 to 3.
The values in the subtree of node 1: {1,2,3}. Since node.val == 1, there are no nodes having a smaller value than its value. So it&#39;s not great enough.
The values in the subtree of node 2: {2}. Since node.val == 2, there are no nodes having a smaller value than its value. So it&#39;s not great enough.
The values in the subtree of node 3: {3}. Since node.val == 3, there are no nodes having a smaller value than its value. So it&#39;s not great enough.
See the picture below for a better understanding.</pre>

<p><img alt="" src="https://assets.leetcode.com/uploads/2023/07/25/2.png" style="padding: 10px; background: rgb(255, 255, 255); border-radius: 0.5rem; width: 123px; height: 101px;" /></p>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> root = [3,2,2], k = 2
<strong>Output:</strong> 1
<strong>Explanation: </strong>Number the nodes from 1 to 3.
The values in the subtree of node 1: {2,2,3}. Since node.val == 3, there are 2 nodes having a smaller value than its value. So it&#39;s great enough.
The values in the subtree of node 2: {2}. Since node.val == 2, there are no nodes having a smaller value than its value. So it&#39;s not great enough.
The values in the subtree of node 3: {2}. Since node.val == 2, there are no nodes having a smaller value than its value. So it&#39;s not great enough.
See the picture below for a better understanding.</pre>

<p><img alt="" src="https://assets.leetcode.com/uploads/2023/07/25/3.png" style="padding: 10px; background: rgb(255, 255, 255); border-radius: 0.5rem; width: 123px; height: 101px;" /></p>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li>The number of nodes in the tree is in the range&nbsp;<code>[1, 10<sup>4</sup>]</code>.<span style="display: none;">&nbsp;</span></li>
	<li><code>1 &lt;= Node.val &lt;= 10<sup>4</sup></code></li>
	<li><code>1 &lt;= k &lt;= 10</code></li>
</ul>
