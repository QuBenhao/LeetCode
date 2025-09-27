# 976. 三角形的最大周长 [难度分: 1340.56]

<p>给定由一些正数（代表长度）组成的数组 <code>nums</code>&nbsp;，返回 <em>由其中三个长度组成的、<strong>面积不为零</strong>的三角形的最大周长</em>&nbsp;。如果不能形成任何面积不为零的三角形，返回&nbsp;<code>0</code>。</p>

<p>&nbsp;</p>

<ol>
</ol>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>nums = [2,1,2]
<strong>输出：</strong>5
<strong>解释：</strong>你可以用三个边长组成一个三角形:1 2 2。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>nums = [1,2,1,10]
<strong>输出：</strong>0
<strong>解释：</strong>
你不能用边长 1,1,2 来组成三角形。
不能用边长 1,1,10 来构成三角形。
不能用边长 1、2 和 10 来构成三角形。
因为我们不能用任何三条边长来构成一个非零面积的三角形，所以我们返回 0。</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>3 &lt;= nums.length &lt;= 10<sup>4</sup></code></li>
	<li><code>1 &lt;= nums[i] &lt;= 10<sup>6</sup></code></li>
</ul>
