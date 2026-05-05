# 1861. 旋转盒子 [难度分: 1536.70]

<p>给你一个&nbsp;<code>m x n</code>&nbsp;的字符矩阵&nbsp;<code>boxGrid</code>&nbsp;，它表示一个箱子的侧视图。箱子的每一个格子可能为：</p>

<ul>
	<li><code>'#'</code>&nbsp;表示石头</li>
	<li><code>'*'</code>&nbsp;表示固定的障碍物</li>
	<li><code>'.'</code>&nbsp;表示空位置</li>
</ul>

<p>这个箱子被 <strong>顺时针旋转 90 度</strong>&nbsp;，由于重力原因，部分石头的位置会发生改变。每个石头会垂直掉落，直到它遇到障碍物，另一个石头或者箱子的底部。重力 <strong>不会</strong>&nbsp;影响障碍物的位置，同时箱子旋转不会产生<strong>惯性</strong>&nbsp;，也就是说石头的水平位置不会发生改变。</p>

<p>题目保证初始时&nbsp;<code>boxGrid</code>&nbsp;中的石头要么在一个障碍物上，要么在另一个石头上，要么在箱子的底部。</p>

<p>请你返回一个<em>&nbsp;</em><code>n x m</code>&nbsp;的矩阵，表示按照上述旋转后，箱子内的结果。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<p><img alt="" src="https://assets.leetcode.com/uploads/2021/04/08/rotatingtheboxleetcodewithstones.png" style="width: 300px; height: 150px;" /></p>

<pre>
<b>输入：</b>box = [["#",".","#"]]
<b>输出：</b>[["."],
&nbsp;     ["#"],
&nbsp;     ["#"]]
</pre>

<p><strong>示例 2：</strong></p>

<p><img alt="" src="https://assets.leetcode.com/uploads/2021/04/08/rotatingtheboxleetcode2withstones.png" style="width: 375px; height: 195px;" /></p>

<pre>
<b>输入：</b>box = [["#",".","*","."],
&nbsp;           ["#","#","*","."]]
<b>输出：</b>[["#","."],
&nbsp;     ["#","#"],
&nbsp;     ["*","*"],
&nbsp;     [".","."]]
</pre>

<p><strong>示例 3：</strong></p>

<p><img alt="" src="https://assets.leetcode.com/uploads/2021/04/08/rotatingtheboxleetcode3withstone.png" style="width: 400px; height: 218px;" /></p>

<pre>
<b>输入：</b>box = [["#","#","*",".","*","."],
&nbsp;           ["#","#","#","*",".","."],
&nbsp;           ["#","#","#",".","#","."]]
<b>输出：</b>[[".","#","#"],
&nbsp;     [".","#","#"],
&nbsp;     ["#","#","*"],
&nbsp;     ["#","*","."],
&nbsp;     ["#",".","*"],
&nbsp;     ["#",".","."]]
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>m == boxGrid.length</code></li>
	<li><code>n == boxGrid[i].length</code></li>
	<li><code>1 &lt;= m, n &lt;= 500</code></li>
	<li><code>boxGrid[i][j]</code>&nbsp;只可能是&nbsp;<code>'#'</code>&nbsp;，<code>'*'</code>&nbsp;或者&nbsp;<code>'.'</code>&nbsp;。</li>
</ul>
