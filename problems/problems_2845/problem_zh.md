# 2845. 统计趣味子数组的数目 [难度分: 2073.05]

<p>给你一个下标从 <strong>0</strong> 开始的整数数组 <code>nums</code> ，以及整数 <code>modulo</code> 和整数 <code>k</code> 。</p>

<p>请你找出并统计数组中 <strong>趣味子数组</strong> 的数目。</p>

<p>如果 <strong>子数组</strong> <code>nums[l..r]</code> 满足下述条件，则称其为 <strong>趣味子数组</strong> ：</p>

<ul>
	<li>在范围 <code>[l, r]</code> 内，设 <code>cnt</code> 为满足 <code>nums[i] % modulo == k</code> 的索引 <code>i</code> 的数量。并且 <code>cnt % modulo == k</code> 。</li>
</ul>

<p>以整数形式表示并返回趣味子数组的数目。<em> </em></p>

<p><span><strong>注意：</strong>子数组是数组中的一个连续非空的元素序列。</span></p>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>

<pre>
<strong>输入：</strong>nums = [3,2,4], modulo = 2, k = 1
<strong>输出：</strong>3
<strong>解释：</strong>在这个示例中，趣味子数组分别是： 
子数组 nums[0..0] ，也就是 [3] 。 
- 在范围 [0, 0] 内，只存在 1 个下标 i = 0 满足 nums[i] % modulo == k 。
- 因此 cnt = 1 ，且 cnt % modulo == k 。
子数组 nums[0..1] ，也就是 [3,2] 。
- 在范围 [0, 1] 内，只存在 1 个下标 i = 0 满足 nums[i] % modulo == k 。
- 因此 cnt = 1 ，且 cnt % modulo == k 。
子数组 nums[0..2] ，也就是 [3,2,4] 。
- 在范围 [0, 2] 内，只存在 1 个下标 i = 0 满足 nums[i] % modulo == k 。
- 因此 cnt = 1 ，且 cnt % modulo == k 。
可以证明不存在其他趣味子数组。因此，答案为 3 。</pre>

<p><strong class="example">示例 2：</strong></p>

<pre>
<strong>输入：</strong>nums = [3,1,9,6], modulo = 3, k = 0
<strong>输出：</strong>2
<strong>解释：</strong>在这个示例中，趣味子数组分别是： 
子数组 nums[0..3] ，也就是 [3,1,9,6] 。
- 在范围 [0, 3] 内，只存在 3 个下标 i = 0, 2, 3 满足 nums[i] % modulo == k 。
- 因此 cnt = 3 ，且 cnt % modulo == k 。
子数组 nums[1..1] ，也就是 [1] 。
- 在范围 [1, 1] 内，不存在下标满足 nums[i] % modulo == k 。
- 因此 cnt = 0 ，且 cnt % modulo == k 。
可以证明不存在其他趣味子数组，因此答案为 2 。</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 10<sup>5 </sup></code></li>
	<li><code>1 &lt;= nums[i] &lt;= 10<sup>9</sup></code></li>
	<li><code>1 &lt;= modulo &lt;= 10<sup>9</sup></code></li>
	<li><code>0 &lt;= k &lt; modulo</code></li>
</ul>
