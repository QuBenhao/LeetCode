# 2257. 统计网格图中没有被保卫的格子数 [难度分: 1708.71]

<p>给你两个整数&nbsp;<code>m</code>&nbsp;和&nbsp;<code>n</code>&nbsp;表示一个下标从<strong>&nbsp;0</strong>&nbsp;开始的&nbsp;<code>m x n</code>&nbsp;网格图。同时给你两个二维整数数组&nbsp;<code>guards</code> 和&nbsp;<code>walls</code>&nbsp;，其中&nbsp;<code>guards[i] = [row<sub>i</sub>, col<sub>i</sub>]</code>&nbsp;且&nbsp;<code>walls[j] = [row<sub>j</sub>, col<sub>j</sub>]</code>&nbsp;，分别表示第 <code>i</code>&nbsp;个警卫和第 <code>j</code>&nbsp;座墙所在的位置。</p>

<p>一个警卫能看到 4 个坐标轴方向（即东、南、西、北）的 <strong>所有</strong>&nbsp;格子，除非他们被一座墙或者另外一个警卫 <strong>挡住</strong>&nbsp;了视线。如果一个格子能被 <strong>至少</strong>&nbsp;一个警卫看到，那么我们说这个格子被 <strong>保卫</strong>&nbsp;了。</p>

<p>请你返回空格子中，有多少个格子是 <strong>没被保卫</strong>&nbsp;的。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<p><img alt="" src="https://assets.leetcode.com/uploads/2022/03/10/example1drawio2.png" style="width: 300px; height: 204px;"></p>

<pre><b>输入：</b>m = 4, n = 6, guards = [[0,0],[1,1],[2,3]], walls = [[0,1],[2,2],[1,4]]
<b>输出：</b>7
<strong>解释：</strong>上图中，被保卫和没有被保卫的格子分别用红色和绿色表示。
总共有 7 个没有被保卫的格子，所以我们返回 7 。
</pre>

<p><strong>示例 2：</strong></p>

<p><img alt="" src="https://assets.leetcode.com/uploads/2022/03/10/example2drawio.png" style="width: 200px; height: 201px;"></p>

<pre><b>输入：</b>m = 3, n = 3, guards = [[1,1]], walls = [[0,1],[1,0],[2,1],[1,2]]
<b>输出：</b>4
<b>解释：</b>上图中，没有被保卫的格子用绿色表示。
总共有 4 个没有被保卫的格子，所以我们返回 4 。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= m, n &lt;= 10<sup>5</sup></code></li>
	<li><code>2 &lt;= m * n &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= guards.length, walls.length &lt;= 5 * 10<sup>4</sup></code></li>
	<li><code>2 &lt;= guards.length + walls.length &lt;= m * n</code></li>
	<li><code>guards[i].length == walls[j].length == 2</code></li>
	<li><code>0 &lt;= row<sub>i</sub>, row<sub>j</sub> &lt; m</code></li>
	<li><code>0 &lt;= col<sub>i</sub>, col<sub>j</sub> &lt; n</code></li>
	<li><code>guards</code>&nbsp;和&nbsp;<code>walls</code>&nbsp;中所有位置 <strong>互不相同</strong>&nbsp;。</li>
</ul>
