# 2654. 使数组所有元素变成 1 的最少操作次数 [难度分: 1928.80]

<p>给你一个下标从 <strong>0</strong>&nbsp;开始的 <strong>正</strong>&nbsp;整数数组&nbsp;<code>nums</code>&nbsp;。你可以对数组执行以下操作 <strong>任意</strong>&nbsp;次：</p>

<ul>
	<li>选择一个满足&nbsp;<code>0 &lt;= i &lt; n - 1</code>&nbsp;的下标 <code>i</code>&nbsp;，将&nbsp;<code>nums[i]</code> 或者&nbsp;<code>nums[i+1]</code>&nbsp;两者之一替换成它们的最大公约数。</li>
</ul>

<p>请你返回使数组 <code>nums</code>&nbsp;中所有元素都等于 <code>1</code>&nbsp;的 <strong>最少</strong>&nbsp;操作次数。如果无法让数组全部变成 <code>1</code>&nbsp;，请你返回 <code>-1</code>&nbsp;。</p>

<p>两个正整数的最大公约数指的是能整除这两个数的最大正整数。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre><b>输入：</b>nums = [2,6,3,4]
<b>输出：</b>4
<b>解释：</b>我们可以执行以下操作：
- 选择下标 i = 2 ，将 nums[2] 替换为 gcd(3,4) = 1 ，得到 nums = [2,6,1,4] 。
- 选择下标 i = 1 ，将 nums[1] 替换为 gcd(6,1) = 1 ，得到 nums = [2,1,1,4] 。
- 选择下标 i = 0 ，将 nums[0] 替换为 gcd(2,1) = 1 ，得到 nums = [1,1,1,4] 。
- 选择下标 i = 2 ，将 nums[3] 替换为 gcd(1,4) = 1 ，得到 nums = [1,1,1,1] 。
</pre>

<p><strong>示例 2：</strong></p>

<pre><b>输入：</b>nums = [2,10,6,14]
<b>输出：</b>-1
<b>解释：</b>无法将所有元素都变成 1 。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>2 &lt;= nums.length &lt;= 50</code></li>
	<li><code>1 &lt;= nums[i] &lt;= 10<sup>6</sup></code></li>
</ul>
