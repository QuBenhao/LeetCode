# 2773. Height of Special Binary Tree

<p>You are given a <code>root</code>, which is the root of a <strong>special</strong> binary tree with <code>n</code> nodes. The nodes of the special binary tree are numbered from <code>1</code> to <code>n</code>. Suppose the tree has <code>k</code> leaves in the following order: <code>b<sub>1 </sub>&lt;<sub> </sub>b<sub>2 </sub>&lt; ... &lt; b<sub>k</sub></code>.</p>

<p>The leaves of this tree have a <strong>special</strong> property! That is, for every leaf <code>b<sub>i</sub></code>, the following conditions hold:</p>

<ul>
	<li>The right child of <code>b<sub>i</sub></code> is <code>b<sub>i + 1</sub></code> if <code>i &lt; k</code>, and <code>b<sub>1</sub></code> otherwise.</li>
	<li>The left child of <code>b<sub>i</sub></code> is <code>b<sub>i - 1</sub></code> if <code>i &gt; 1</code>, and <code>b<sub>k</sub></code> otherwise.</li>
</ul>

<p>Return<em> the height of the given tree.</em></p>

<p><strong>Note:</strong> The height of a binary tree is the length of the <strong>longest path</strong> from the root to any other node.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> root = [1,2,3,null,null,4,5]
<strong>Output:</strong> 2
<strong>Explanation: </strong>The given tree is shown in the following picture. Each leaf&#39;s left child is the leaf to its left (shown with the blue edges). Each leaf&#39;s right child is the leaf to its right (shown with the red edges). We can see that the graph has a height of 2.
</pre>

<p><img alt="" src="https://assets.leetcode.com/uploads/2023/07/12/1.png" style="padding: 10px; background: rgb(255, 255, 255); border-radius: 0.5rem; width: 200px; height: 200px;" /></p>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> root = [1,2]
<strong>Output:</strong> 1
<strong>Explanation: </strong>The given tree is shown in the following picture. There is only one leaf, so it doesn&#39;t have any left or right child. We can see that the graph has a height of 1.
</pre>

<p><img alt="" src="https://assets.leetcode.com/uploads/2023/07/12/2.png" style="padding: 10px; background: rgb(255, 255, 255); border-radius: 0.5rem; width: 95px; height: 122px;" /></p>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> root = [1,2,3,null,null,4,null,5,6]
<strong>Output:</strong> 3
<strong>Explanation: </strong>The given tree is shown in the following picture. Each leaf&#39;s left child is the leaf to its left (shown with the blue edges). Each leaf&#39;s right child is the leaf to its right (shown with the red edges). We can see that the graph has a height of 3.
</pre>

<p><img alt="" src="https://assets.leetcode.com/uploads/2023/07/12/3.png" style="padding: 10px; background: rgb(255, 255, 255); border-radius: 0.5rem; width: 200px; height: 280px;" /></p>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>n == number of nodes in the tree</code></li>
	<li><code>2 &lt;= n &lt;= 10<sup>4</sup></code></li>
	<li><code>1 &lt;= node.val &lt;= n</code></li>
	<li>The input is generated such that each <code>node.val</code> is unique.</li>
</ul>
