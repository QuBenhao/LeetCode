# 2535. 数组元素和与数字和的绝对差 [难度分: 1222.24]

<p>给你一个正整数数组 <code>nums</code> 。</p>

<ul>
	<li><strong>元素和</strong> 是 <code>nums</code> 中的所有元素相加求和。</li>
	<li><strong>数字和</strong> 是&nbsp;<code>nums</code> 中每一个元素的每一数位（重复数位需多次求和）相加求和。</li>
</ul>

<p>返回 <strong>元素和</strong> 与 <strong>数字和</strong> 的绝对差。</p>

<p><strong>注意：</strong>两个整数 <code>x</code> 和 <code>y</code> 的绝对差定义为 <code>|x - y|</code> 。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>nums = [1,15,6,3]
<strong>输出：</strong>9
<strong>解释：</strong>
nums 的元素和是 1 + 15 + 6 + 3 = 25 。
nums 的数字和是 1 + 1 + 5 + 6 + 3 = 16 。
元素和与数字和的绝对差是 |25 - 16| = 9 。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>nums = [1,2,3,4]
<strong>输出：</strong>0
<strong>解释：</strong>
nums 的元素和是 1 + 2 + 3 + 4 = 10 。
nums 的数字和是 1 + 2 + 3 + 4 = 10 。
元素和与数字和的绝对差是 |10 - 10| = 0 。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 2000</code></li>
	<li><code>1 &lt;= nums[i] &lt;= 2000</code></li>
</ul>
