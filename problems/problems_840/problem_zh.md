# 840. 矩阵中的幻方 [难度分: 1425.97]

<p><code>3 x 3</code> 的幻方是一个填充有&nbsp;<strong>从 <code>1</code> 到 <code>9</code>&nbsp;</strong> 的不同数字的 <code>3 x 3</code> 矩阵，其中每行，每列以及两条对角线上的各数之和都相等。</p>

<p>给定一个由整数组成的<code>row x col</code>&nbsp;的 <code>grid</code>，其中有多少个&nbsp;<code>3 × 3</code> 的 “幻方” 子矩阵？</p>

<p>注意：虽然幻方只能包含 1 到 9 的数字，但&nbsp;<code>grid</code> 可以包含最多15的数字。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<p><img src="https://assets.leetcode.com/uploads/2020/09/11/magic_main.jpg" /></p>

<pre>
<strong>输入: </strong>grid = [[4,3,8,4],[9,5,1,9],[2,7,6,2]
<strong>输出: </strong>1
<strong>解释: </strong>
下面的子矩阵是一个 3 x 3 的幻方：
<img src="https://assets.leetcode.com/uploads/2020/09/11/magic_valid.jpg" />
而这一个不是：
<img src="https://assets.leetcode.com/uploads/2020/09/11/magic_invalid.jpg" />
总的来说，在本示例所给定的矩阵中只有一个 3 x 3 的幻方子矩阵。
</pre>

<p><strong>示例 2:</strong></p>

<pre>
<strong>输入:</strong> grid = [[8]]
<strong>输出:</strong> 0
</pre>

<p>&nbsp;</p>

<p><strong>提示:</strong></p>

<ul>
	<li><code>row == grid.length</code></li>
	<li><code>col == grid[i].length</code></li>
	<li><code>1 &lt;= row, col &lt;= 10</code></li>
	<li><code>0 &lt;= grid[i][j] &lt;= 15</code></li>
</ul>
