# 3242. 设计相邻元素求和服务 [难度分: 1334.36]

<p>给你一个 <code>n x n</code> 的二维数组 <code>grid</code>，它包含范围 <code>[0, n<sup>2</sup> - 1]</code> 内的<strong>不重复</strong>元素。</p>

<p>实现 <code>neighborSum</code> 类：</p>

<ul>
	<li><code>neighborSum(int [][]grid)</code> 初始化对象。</li>
	<li><code>int adjacentSum(int value)</code> 返回在 <code>grid</code> 中与 <code>value</code> 相邻的元素之<strong>和</strong>，相邻指的是与 <code>value</code> 在上、左、右或下的元素。</li>
	<li><code>int diagonalSum(int value)</code> 返回在 <code>grid</code> 中与 <code>value</code> 对角线相邻的元素之<strong>和</strong>，对角线相邻指的是与 <code>value</code> 在左上、右上、左下或右下的元素。</li>
</ul>

<p><img alt="" src="https://assets.leetcode.com/uploads/2024/06/24/design.png" style="width: 400px; height: 248px;" /></p>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>

<div class="example-block">
<p><strong>输入：</strong></p>

<p>["neighborSum", "adjacentSum", "adjacentSum", "diagonalSum", "diagonalSum"]</p>

<p>[[[[0, 1, 2], [3, 4, 5], [6, 7, 8]]], [1], [4], [4], [8]]</p>

<p><strong>输出：</strong> [null, 6, 16, 16, 4]</p>

<p><strong>解释：</strong></p>

<p><strong class="example"><img alt="" src="https://assets.leetcode.com/uploads/2024/06/24/designexample0.png" style="width: 250px; height: 249px;" /></strong></p>

<ul>
	<li>1 的相邻元素是 0、2 和 4。</li>
	<li>4 的相邻元素是 1、3、5 和 7。</li>
	<li>4 的对角线相邻元素是 0、2、6 和 8。</li>
	<li>8 的对角线相邻元素是 4。</li>
</ul>
</div>

<p><strong class="example">示例 2：</strong></p>

<div class="example-block">
<p><strong>输入：</strong></p>

<p>["neighborSum", "adjacentSum", "diagonalSum"]</p>

<p>[[[[1, 2, 0, 3], [4, 7, 15, 6], [8, 9, 10, 11], [12, 13, 14, 5]]], [15], [9]]</p>

<p><strong>输出：</strong> [null, 23, 45]</p>

<p><strong>解释：</strong></p>

<p><strong class="example"><img alt="" src="https://assets.leetcode.com/uploads/2024/06/24/designexample2.png" style="width: 300px; height: 300px;" /></strong></p>

<ul>
	<li>15 的相邻元素是 0、10、7 和 6。</li>
	<li>9 的对角线相邻元素是 4、12、14 和 15。</li>
</ul>
</div>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>3 &lt;= n == grid.length == grid[0].length &lt;= 10</code></li>
	<li><code>0 &lt;= grid[i][j] &lt;= n<sup>2</sup> - 1</code></li>
	<li>所有 <code>grid[i][j]</code> 值均不重复。</li>
	<li><code>adjacentSum</code> 和 <code>diagonalSum</code> 中的 <code>value</code> 均在范围 <code>[0, n<sup>2</sup> - 1]</code> 内。</li>
	<li>最多会调用 <code>adjacentSum</code> 和 <code>diagonalSum</code> 总共 <code>2 * n<sup>2</sup></code> 次。</li>
</ul>
