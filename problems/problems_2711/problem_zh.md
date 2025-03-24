# 2711. 对角线上不同值的数量差 [难度分: 1428.72]

<p>给你一个下标从 <code>0</code> 开始、大小为 <code>m x n</code> 的二维矩阵 <code>grid</code> ，请你求解大小同样为 <code>m x n</code> 的答案矩阵 <code>answer</code> 。</p>

<p>矩阵 <code>answer</code> 中每个单元格 <code>(r, c)</code> 的值可以按下述方式进行计算：</p>

<ul>
	<li>令 <code>topLeft[r][c]</code> 为矩阵 <code>grid</code> 中单元格 <code>(r, c)</code> 左上角对角线上 <strong>不同值</strong> 的数量。</li>
	<li>令 <code>bottomRight[r][c]</code> 为矩阵 <code>grid</code> 中单元格 <code>(r, c)</code> 右下角对角线上 <strong>不同值</strong> 的数量。</li>
</ul>

<p>然后 <code>answer[r][c] = |topLeft[r][c] - bottomRight[r][c]|</code> 。</p>

<p>返回矩阵 <code>answer</code> 。</p>

<p><strong>矩阵对角线</strong> 是从最顶行或最左列的某个单元格开始，向右下方向走到矩阵末尾的对角线。</p>

<p>如果单元格 <code>(r1, c1)</code> 和单元格 <code>(r, c) </code>属于同一条对角线且 <code>r1 &lt; r</code> ，则单元格 <code>(r1, c1)</code> 属于单元格 <code>(r, c)</code> 的左上对角线。类似地，可以定义右下对角线。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2023/04/19/ex2.png" style="width: 786px; height: 121px;" />
<pre>
<strong>输入：</strong>grid = [[1,2,3],[3,1,5],[3,2,1]]
<strong>输出：</strong>[[1,1,0],[1,0,1],[0,1,1]]
<strong>解释：</strong>第 1 个图表示最初的矩阵 grid 。&nbsp;
第 2 个图表示对单元格 (0,0) 计算，其中蓝色单元格是位于右下对角线的单元格。
第 3 个图表示对单元格 (1,2) 计算，其中红色单元格是位于左上对角线的单元格。
第 4 个图表示对单元格 (1,1) 计算，其中蓝色单元格是位于右下对角线的单元格，红色单元格是位于左上对角线的单元格。
- 单元格 (0,0) 的右下对角线包含 [1,1] ，而左上对角线包含 [] 。对应答案是 |1 - 0| = 1 。
- 单元格 (1,2) 的右下对角线包含 [] ，而左上对角线包含 [2] 。对应答案是 |0 - 1| = 1 。
- 单元格 (1,1) 的右下对角线包含 [1] ，而左上对角线包含 [1] 。对应答案是 |1 - 1| = 0 。
其他单元格的对应答案也可以按照这样的流程进行计算。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>grid = [[1]]
<strong>输出：</strong>[[0]]
<strong>解释：</strong>- 单元格 (0,0) 的右下对角线包含 [] ，左上对角线包含 [] 。对应答案是 |0 - 0| = 0 。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>m == grid.length</code></li>
	<li><code>n == grid[i].length</code></li>
	<li><code>1 &lt;= m, n, grid[i][j] &lt;= 50</code></li>
</ul>
