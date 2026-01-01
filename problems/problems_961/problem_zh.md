# 961. 在长度 2N 的数组中找出重复 N 次的元素 [难度分: 1161.62]

<p>给你一个整数数组 <code>nums</code> ，该数组具有以下属性：</p>

<div class="original__bRMd">
<div>
<ul>
	<li><code>nums.length == 2 * n</code>.</li>
	<li><code>nums</code> 包含 <code>n + 1</code> 个 <strong>不同的</strong> 元素</li>
	<li><code>nums</code> 中恰有一个元素重复 <code>n</code> 次</li>
</ul>

<p>找出并返回重复了 <code>n</code><em> </em>次的那个元素。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>nums = [1,2,3,3]
<strong>输出：</strong>3
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>nums = [2,1,2,5,3,2]
<strong>输出：</strong>2
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>nums = [5,1,5,2,5,3,5,4]
<strong>输出：</strong>5
</pre>
</div>
</div>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>2 &lt;= n &lt;= 5000</code></li>
	<li><code>nums.length == 2 * n</code></li>
	<li><code>0 &lt;= nums[i] &lt;= 10<sup>4</sup></code></li>
	<li><code>nums</code> 由 <code>n + 1</code> 个<strong> 不同的</strong> 元素组成，且其中一个元素恰好重复 <code>n</code> 次</li>
</ul>
