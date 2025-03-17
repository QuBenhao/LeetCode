# 2614. 对角线上的质数 [难度分: 1375.43]

<p>给你一个下标从 <strong>0</strong> 开始的二维整数数组 <code>nums</code> 。</p>

<p>返回位于 <code>nums</code> 至少一条 <strong>对角线</strong> 上的最大 <strong>质数</strong> 。如果任一对角线上均不存在质数，返回<em> 0 。</em></p>

<p>注意：</p>

<ul>
	<li>如果某个整数大于 <code>1</code> ，且不存在除 <code>1</code> 和自身之外的正整数因子，则认为该整数是一个质数。</li>
	<li>如果存在整数 <code>i</code> ，使得&nbsp;<code>nums[i][i] = val</code> 或者&nbsp;<code>nums[i][nums.length - i - 1]= val</code> ，则认为整数 <code>val</code> 位于 <code>nums</code> 的一条对角线上。</li>
</ul>

<p><img alt="" src="https://assets.leetcode.com/uploads/2023/03/06/screenshot-2023-03-06-at-45648-pm.png" style="width: 181px; height: 121px;" /></p>

<p>在上图中，一条对角线是 <strong>[1,5,9]</strong> ，而另一条对角线是<strong> [3,5,7]</strong> 。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>nums = [[1,2,3],[5,6,7],[9,10,11]]
<strong>输出：</strong>11
<strong>解释：</strong>数字 1、3、6、9 和 11 是所有 "位于至少一条对角线上" 的数字。由于 11 是最大的质数，故返回 11 。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>nums = [[1,2,3],[5,17,7],[9,11,10]]
<strong>输出：</strong>17
<strong>解释：</strong>数字 1、3、9、10 和 17 是所有满足"位于至少一条对角线上"的数字。由于 17 是最大的质数，故返回 17 。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 300</code></li>
	<li><code>nums.length == nums<sub>i</sub>.length</code></li>
	<li><code>1 &lt;= nums<span style="">[i][j]</span>&nbsp;&lt;= 4*10<sup>6</sup></code></li>
</ul>
