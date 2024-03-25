# 3004. Maximum Subtree of the Same Color

<p>You are given a 2D integer array <code>edges</code> representing a tree with <code>n</code> nodes, numbered from <code>0</code> to <code>n - 1</code>, rooted at node <code>0</code>, where <code>edges[i] = [u<sub>i</sub>, v<sub>i</sub>]</code> means there is an edge between the nodes <code>v<sub>i</sub></code> and <code>u<sub>i</sub></code>.</p>

<p>You are also given a <strong>0-indexed</strong> integer array <code>colors</code> of size <code>n</code>, where <code>colors[i]</code> is the color assigned to node <code>i</code>.</p>

<p>We want to find a node <code>v</code> such that every node in the <span data-keyword="subtree-of-node">subtree</span> of <code>v</code> has the <strong>same</strong> color.</p>

<p>Return <em>the size of such subtree with the <strong>maximum</strong> number of nodes possible.</em></p>

<p>&nbsp;</p>
<p><strong><img alt="" src="https://assets.leetcode.com/static_assets/others/20231216-134026.png" style="padding: 10px; background: rgb(255, 255, 255); border-radius: 0.5rem; width: 221px; height: 132px;" /></strong></p>

<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> edges = [[0,1],[0,2],[0,3]], colors = [1,1,2,3]
<strong>Output:</strong> 1
<strong>Explanation:</strong> Each color is represented as: 1 -&gt; Red, 2 -&gt; Green, 3 -&gt; Blue. We can see that the subtree rooted at node 0 has children with different colors. Any other subtree is of the same color and has a size of 1. Hence, we return 1.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> edges = [[0,1],[0,2],[0,3]], colors = [1,1,1,1]
<strong>Output:</strong> 4
<strong>Explanation:</strong> The whole tree has the same color, and the subtree rooted at node 0 has the most number of nodes which is 4. Hence, we return 4.
</pre>

<p><strong><img alt="" src="https://assets.leetcode.com/static_assets/others/20231216-134017.png" style="padding: 10px; background: rgb(255, 255, 255); border-radius: 0.5rem; width: 221px; height: 221px;" /></strong></p>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> edges = [[0,1],[0,2],[2,3],[2,4]], colors = [1,2,3,3,3]
<strong>Output:</strong> 3
<strong>Explanation:</strong> Each color is represented as: 1 -&gt; Red, 2 -&gt; Green, 3 -&gt; Blue. We can see that the subtree rooted at node 0 has children with different colors. Any other subtree is of the same color, but the subtree rooted at node 2 has a size of 3 which is the maximum. Hence, we return 3.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>n == edges.length + 1</code></li>
	<li><code>1 &lt;= n &lt;= 5 * 10<sup>4</sup></code></li>
	<li><code>edges[i] == [u<sub>i</sub>, v<sub>i</sub>]</code></li>
	<li><code>0 &lt;= u<sub>i</sub>, v<sub>i</sub> &lt; n</code></li>
	<li><code>colors.length == n</code></li>
	<li><code>1 &lt;= colors[i] &lt;= 10<sup>5</sup></code></li>
	<li>The input is generated such that the graph represented by <code>edges</code> is a tree.</li>
</ul>
