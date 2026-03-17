# 3070. 元素和小于等于 k 的子矩阵的数目 [难度分: 1498.69]

<p>给你一个下标从 <strong>0</strong> 开始的整数矩阵 <code>grid</code> 和一个整数 <code>k</code>。</p>

<p>返回包含 <code>grid</code> 左上角元素、元素和小于或等于 <code>k</code> 的 <strong><span data-keyword="submatrix">子矩阵</span></strong>的数目。</p>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2024/01/01/example1.png" style="padding: 10px; background: #fff; border-radius: .5rem;" />
<pre>
<strong>输入：</strong>grid = [[7,6,3],[6,6,1]], k = 18
<strong>输出：</strong>4
<strong>解释：</strong>如上图所示，只有 4 个子矩阵满足：包含 grid 的左上角元素，并且元素和小于或等于 18 。</pre>

<p><strong class="example">示例 2：</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2024/01/01/example21.png" style="padding: 10px; background: #fff; border-radius: .5rem;" />
<pre>
<strong>输入：</strong>grid = [[7,2,9],[1,5,0],[2,6,6]], k = 20
<strong>输出：</strong>6
<strong>解释：</strong>如上图所示，只有 6 个子矩阵满足：包含 grid 的左上角元素，并且元素和小于或等于 20 。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>m == grid.length </code></li>
	<li><code>n == grid[i].length</code></li>
	<li><code>1 &lt;= n, m &lt;= 1000 </code></li>
	<li><code>0 &lt;= grid[i][j] &lt;= 1000</code></li>
	<li><code>1 &lt;= k &lt;= 10<sup>9</sup></code></li>
</ul>
