# 2435. 矩阵中和能被 K 整除的路径 [难度分: 1951.59]

<p>给你一个下标从 <strong>0</strong>&nbsp;开始的&nbsp;<code>m x n</code>&nbsp;整数矩阵&nbsp;<code>grid</code>&nbsp;和一个整数&nbsp;<code>k</code>&nbsp;。你从起点&nbsp;<code>(0, 0)</code>&nbsp;出发，每一步只能往 <strong>下</strong>&nbsp;或者往 <strong>右</strong>&nbsp;，你想要到达终点&nbsp;<code>(m - 1, n - 1)</code>&nbsp;。</p>

<p>请你返回路径和能被 <code>k</code>&nbsp;整除的路径数目，由于答案可能很大，返回答案对&nbsp;<code>10<sup>9</sup> + 7</code>&nbsp;<strong>取余</strong>&nbsp;的结果。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<p><img src="https://assets.leetcode.com/uploads/2022/08/13/image-20220813183124-1.png" style="width: 437px; height: 200px;"></p>

<pre><b>输入：</b>grid = [[5,2,4],[3,0,5],[0,7,2]], k = 3
<b>输出：</b>2
<b>解释：</b>有两条路径满足路径上元素的和能被 k 整除。
第一条路径为上图中用红色标注的路径，和为 5 + 2 + 4 + 5 + 2 = 18 ，能被 3 整除。
第二条路径为上图中用蓝色标注的路径，和为 5 + 3 + 0 + 5 + 2 = 15 ，能被 3 整除。
</pre>

<p><strong>示例 2：</strong></p>
<img src="https://assets.leetcode.com/uploads/2022/08/17/image-20220817112930-3.png" style="height: 85px; width: 132px;">
<pre><b>输入：</b>grid = [[0,0]], k = 5
<b>输出：</b>1
<b>解释：</b>红色标注的路径和为 0 + 0 = 0 ，能被 5 整除。
</pre>

<p><strong>示例 3：</strong></p>
<img src="https://assets.leetcode.com/uploads/2022/08/12/image-20220812224605-3.png" style="width: 257px; height: 200px;">
<pre><b>输入：</b>grid = [[7,3,4,9],[2,3,6,2],[2,3,7,0]], k = 1
<b>输出：</b>10
<b>解释：</b>每个数字都能被 1 整除，所以每一条路径的和都能被 k 整除。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>m == grid.length</code></li>
	<li><code>n == grid[i].length</code></li>
	<li><code>1 &lt;= m, n &lt;= 5 * 10<sup>4</sup></code></li>
	<li><code>1 &lt;= m * n &lt;= 5 * 10<sup>4</sup></code></li>
	<li><code>0 &lt;= grid[i][j] &lt;= 100</code></li>
	<li><code>1 &lt;= k &lt;= 50</code></li>
</ul>
