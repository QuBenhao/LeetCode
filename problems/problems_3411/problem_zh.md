# 3411. 最长乘积等价子数组 [难度分: 1443.19]

<p>给你一个由&nbsp;<strong>正整数&nbsp;</strong>组成的数组 <code>nums</code>。</p>

<p>如果一个数组 <code>arr</code> 满足 <code>prod(arr) == lcm(arr) * gcd(arr)</code>，则称其为&nbsp;<strong>乘积等价数组&nbsp;</strong>，其中：</p>

<ul>
	<li><code>prod(arr)</code> 表示 <code>arr</code> 中所有元素的乘积。</li>
	<li><code>gcd(arr)</code> 表示 <code>arr</code> 中所有元素的最大公因数 (<span data-keyword="gcd-function">GCD</span>)。</li>
	<li><code>lcm(arr)</code> 表示 <code>arr</code> 中所有元素的最小公倍数 (<span data-keyword="lcm-function">LCM</span>)。</li>
</ul>

<p>返回数组 <code>nums</code> 的&nbsp;<strong>最长</strong> <strong>乘积等价 <span data-keyword="subarray-nonempty">子数组</span>&nbsp;</strong>的长度。</p>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>

<div class="example-block">
<p><strong>输入：</strong> <span class="example-io">nums = [1,2,1,2,1,1,1]</span></p>

<p><strong>输出：</strong> <span class="example-io">5</span></p>

<p><strong>解释：</strong>&nbsp;</p>

<p>最长的乘积等价子数组是 <code>[1, 2, 1, 1, 1]</code>，其中&nbsp;<code>prod([1, 2, 1, 1, 1]) = 2</code>，&nbsp;<code>gcd([1, 2, 1, 1, 1]) = 1</code>，以及&nbsp;<code>lcm([1, 2, 1, 1, 1]) = 2</code>。</p>
</div>

<p><strong class="example">示例 2：</strong></p>

<div class="example-block">
<p><strong>输入：</strong> <span class="example-io">nums = [2,3,4,5,6]</span></p>

<p><strong>输出：</strong> <span class="example-io">3</span></p>

<p><strong>解释：</strong>&nbsp;</p>

<p>最长的乘积等价子数组是 <code>[3, 4, 5]</code>。</p>
</div>

<p><strong class="example">示例 3：</strong></p>

<div class="example-block">
<p><strong>输入：</strong> <span class="example-io">nums = [1,2,3,1,4,5,1]</span></p>

<p><strong>输出：</strong> <span class="example-io">5</span></p>
</div>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>2 &lt;= nums.length &lt;= 100</code></li>
	<li><code>1 &lt;= nums[i] &lt;= 10</code></li>
</ul>
