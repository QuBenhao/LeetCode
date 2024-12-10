# 2717. 半有序排列 [难度分: 1295.76]

<p>给你一个下标从 <strong>0</strong> 开始、长度为 <code>n</code> 的整数排列 <code>nums</code> 。</p>

<p>如果排列的第一个数字等于 <code>1</code> 且最后一个数字等于 <code>n</code> ，则称其为 <strong>半有序排列</strong> 。你可以执行多次下述操作，直到将 <code>nums</code> 变成一个 <strong>半有序排列</strong> ：</p>

<ul>
	<li>选择 <code>nums</code> 中相邻的两个元素，然后交换它们。</li>
</ul>

<p>返回使 <code>nums</code> 变成 <strong>半有序排列</strong> 所需的最小操作次数。</p>

<p><strong>排列</strong> 是一个长度为 <code>n</code> 的整数序列，其中包含从 <code>1</code> 到 <code>n</code> 的每个数字恰好一次。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>nums = [2,1,4,3]
<strong>输出：</strong>2
<strong>解释：</strong>可以依次执行下述操作得到半有序排列：
1 - 交换下标 0 和下标 1 对应元素。排列变为 [1,2,4,3] 。
2 - 交换下标 2 和下标 3 对应元素。排列变为 [1,2,3,4] 。
可以证明，要让 nums 成为半有序排列，不存在执行操作少于 2 次的方案。</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>nums = [2,4,1,3]
<strong>输出：</strong>3
<strong>解释：
</strong>可以依次执行下述操作得到半有序排列：
1 - 交换下标 1 和下标 2 对应元素。排列变为 [2,1,4,3] 。
2 - 交换下标 0 和下标 1 对应元素。排列变为 [1,2,4,3] 。
3 - 交换下标 2 和下标 3 对应元素。排列变为 [1,2,3,4] 。
可以证明，要让 nums 成为半有序排列，不存在执行操作少于 3 次的方案。
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>nums = [1,3,4,2,5]
<strong>输出：</strong>0
<strong>解释：</strong>这个排列已经是一个半有序排列，无需执行任何操作。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>2 &lt;= nums.length == n &lt;= 50</code></li>
	<li><code>1 &lt;= nums[i]&nbsp;&lt;= 50</code></li>
	<li><code>nums</code> 是一个 <strong>排列</strong></li>
</ul>
