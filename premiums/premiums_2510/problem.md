# 2510. Check if There is a Path With Equal Number of 0's And 1's

<p>You are given a <strong>0-indexed</strong> <code>m x n</code> <strong>binary</strong> matrix <code>grid</code>. You can move from a cell <code>(row, col)</code> to any of the cells <code>(row + 1, col)</code> or <code>(row, col + 1)</code>.</p>

<p>Return <code>true</code><em> if there is a path from </em><code>(0, 0)</code><em> to </em><code>(m - 1, n - 1)</code><em> that visits an <strong>equal</strong> number of </em><code>0</code><em>&#39;s and </em><code>1</code><em>&#39;s</em>. Otherwise return <code>false</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2022/12/20/yetgriddrawio-4.png" />
<pre>
<strong>Input:</strong> grid = [[0,1,0,0],[0,1,0,0],[1,0,1,0]]
<strong>Output:</strong> true
<strong>Explanation:</strong> The path colored in blue in the above diagram is a valid path because we have 3 cells with a value of 1 and 3 with a value of 0. Since there is a valid path, we return true.
</pre>

<p><strong class="example">Example 2:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2022/12/20/yetgrid2drawio-1.png" style="width: 151px; height: 151px;" />
<pre>
<strong>Input:</strong> grid = [[1,1,0],[0,0,1],[1,0,0]]
<strong>Output:</strong> false
<strong>Explanation:</strong> There is no path in this grid with an equal number of 0&#39;s and 1&#39;s.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>m == grid.length</code></li>
	<li><code>n == grid[i].length</code></li>
	<li><code>2 &lt;= m, n &lt;= 100</code></li>
	<li><code>grid[i][j]</code> is either <code>0</code> or <code>1</code>.</li>
</ul>
