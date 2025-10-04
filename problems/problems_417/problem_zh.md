# 417. 太平洋大西洋水流问题 

<p>有一个 <code>m × n</code> 的矩形岛屿，与 <strong>太平洋</strong> 和 <strong>大西洋</strong> 相邻。&nbsp;<strong>“太平洋”&nbsp;</strong>处于大陆的左边界和上边界，而 <strong>“大西洋”</strong> 处于大陆的右边界和下边界。</p>

<p>这个岛被分割成一个由若干方形单元格组成的网格。给定一个 <code>m x n</code> 的整数矩阵&nbsp;<code>heights</code>&nbsp;，&nbsp;<code>heights[r][c]</code>&nbsp;表示坐标 <code>(r, c)</code> 上单元格 <strong>高于海平面的高度</strong> 。</p>

<p>岛上雨水较多，如果相邻单元格的高度 <strong>小于或等于</strong> 当前单元格的高度，雨水可以直接向北、南、东、西流向相邻单元格。水可以从海洋附近的任何单元格流入海洋。</p>

<p>返回网格坐标 <code>result</code>&nbsp;的 <strong>2D 列表</strong> ，其中&nbsp;<code>result[i] = [r<sub>i</sub>, c<sub>i</sub>]</code>&nbsp;表示雨水从单元格 <code>(ri, ci)</code> 流动 <strong>既可流向太平洋也可流向大西洋</strong> 。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<p><img src="https://assets.leetcode.com/uploads/2021/06/08/waterflow-grid.jpg" /></p>

<pre>
<strong>输入:</strong> heights = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
<strong>输出:</strong> [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入:</strong> heights = [[2,1],[1,2]]
<strong>输出:</strong> [[0,0],[0,1],[1,0],[1,1]]
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>m == heights.length</code></li>
	<li><code>n == heights[r].length</code></li>
	<li><code>1 &lt;= m, n &lt;= 200</code></li>
	<li><code>0 &lt;= heights[r][c] &lt;= 10<sup>5</sup></code></li>
</ul>
