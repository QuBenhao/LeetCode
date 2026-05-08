# 1914. 循环轮转矩阵 [难度分: 1766.25]

<p>给你一个大小为 <code>m x n</code> 的整数矩阵 <code>grid</code>​​​ ，其中 <code>m</code> 和 <code>n</code> 都是 <strong>偶数</strong> ；另给你一个整数 <code>k</code> 。</p>

<p>矩阵由若干层组成，如下图所示，每种颜色代表一层：</p>

<p><img alt="" src="https://assets.leetcode.com/uploads/2021/06/10/ringofgrid.png" style="width: 231px; height: 258px;"></p>

<p>矩阵的循环轮转是通过分别循环轮转矩阵中的每一层完成的。在对某一层进行一次循环旋转操作时，层中的每一个元素将会取代其 <strong>逆时针 </strong>方向的相邻元素。轮转示例如下：</p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/06/22/explanation_grid.jpg" style="width: 500px; height: 268px;">
<p>返回执行 <code>k</code> 次循环轮转操作后的矩阵。</p>

<p> </p>

<p><strong>示例 1：</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/06/19/rod2.png" style="width: 421px; height: 191px;">
<pre><strong>输入：</strong>grid = [[40,10],[30,20]], k = 1
<strong>输出：</strong>[[10,20],[40,30]]
<strong>解释：</strong>上图展示了矩阵在执行循环轮转操作时每一步的状态。</pre>

<p><strong>示例 2：</strong></p>
<strong><img alt="" src="https://assets.leetcode.com/uploads/2021/06/10/ringofgrid5.png" style="width: 231px; height: 262px;"></strong> <strong><img alt="" src="https://assets.leetcode.com/uploads/2021/06/10/ringofgrid6.png" style="width: 231px; height: 262px;"></strong> <strong><img alt="" src="https://assets.leetcode.com/uploads/2021/06/10/ringofgrid7.png" style="width: 231px; height: 262px;"></strong>

<pre><strong>输入：</strong>grid = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]], k = 2
<strong>输出：</strong>[[3,4,8,12],[2,11,10,16],[1,7,6,15],[5,9,13,14]]
<strong>解释：</strong>上图展示了矩阵在执行循环轮转操作时每一步的状态。
</pre>

<p> </p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>m == grid.length</code></li>
	<li><code>n == grid[i].length</code></li>
	<li><code>2 &lt;= m, n &lt;= 50</code></li>
	<li><code>m</code> 和 <code>n</code> 都是 <strong>偶数</strong></li>
	<li><code>1 &lt;= grid[i][j] &lt;=<sup> </sup>5000</code></li>
	<li><code>1 &lt;= k &lt;= 10<sup>9</sup></code></li>
</ul>
