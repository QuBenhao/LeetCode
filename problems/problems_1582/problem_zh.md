# 1582. 二进制矩阵中的特殊位置 [难度分: 1321.27]

<p>给定一个 <code>m x n</code> 的二进制矩阵 <code>mat</code>，返回矩阵 <code>mat</code> 中特殊位置的数量。</p>

<p>如果位置 <code>(i, j)</code> 满足 <code>mat[i][j] == 1</code> 并且行 <code>i</code> 与列 <code>j</code> 中的所有其他元素都是 <code>0</code>（行和列的下标从 <strong>0 </strong>开始计数），那么它被称为<strong> 特殊 </strong>位置。</p>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/12/23/special1.jpg" style="width: 244px; height: 245px;" />
<pre>
<strong>输入：</strong>mat = [[1,0,0],[0,0,1],[1,0,0]]
<strong>输出：</strong>1
<strong>解释：</strong>位置 (1, 2) 是一个特殊位置，因为 mat[1][2] == 1 且第 1 行和第 2 列的其他所有元素都是 0。
</pre>

<p><strong class="example">示例 2：</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/12/24/special-grid.jpg" style="width: 244px; height: 245px;" />
<pre>
<strong>输入：</strong>mat = [[1,0,0],[0,1,0],[0,0,1]]
<strong>输出：</strong>3
<strong>解释：</strong>位置 (0, 0)，(1, 1) 和 (2, 2) 都是特殊位置。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>m == mat.length</code></li>
	<li><code>n == mat[i].length</code></li>
	<li><code>1 &lt;= m, n &lt;= 100</code></li>
	<li><code>mat[i][j]</code> 是 <code>0</code> 或 <code>1</code>。</li>
</ul>
