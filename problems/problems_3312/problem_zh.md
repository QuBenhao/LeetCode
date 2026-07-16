# 3312. 查询排序后的最大公约数 [难度分: 2532.63]

<p>给你一个长度为 <code>n</code>&nbsp;的整数数组&nbsp;<code>nums</code>&nbsp;和一个整数数组&nbsp;<code>queries</code>&nbsp;。</p>

<p><code>gcdPairs</code>&nbsp;表示数组 <code>nums</code>&nbsp;中所有满足 <code>0 &lt;= i &lt; j &lt; n</code>&nbsp;的数对 <code>(nums[i], nums[j])</code> 的 <span data-keyword="gcd-function">最大公约数</span> <strong>升序</strong>&nbsp;排列构成的数组。</p>

<p>对于每个查询&nbsp;<code>queries[i]</code>&nbsp;，你需要找到&nbsp;<code>gcdPairs</code>&nbsp;中下标为&nbsp;<code>queries[i]</code>&nbsp;的元素。</p>


<p>请你返回一个整数数组&nbsp;<code>answer</code>&nbsp;，其中&nbsp;<code>answer[i]</code>&nbsp;是&nbsp;<code>gcdPairs[queries[i]]</code>&nbsp;的值。</p>

<p><code>gcd(a, b)</code>&nbsp;表示 <code>a</code>&nbsp;和 <code>b</code>&nbsp;的 <strong>最大公约数</strong>&nbsp;。</p>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>

<div class="example-block">
<p><span class="example-io"><b>输入：</b>nums = [2,3,4], queries = [0,2,2]</span></p>

<p><span class="example-io"><b>输出：</b>[1,2,2]</span></p>

<p><strong>解释：</strong></p>

<p><code>gcdPairs = [gcd(nums[0], nums[1]), gcd(nums[0], nums[2]), gcd(nums[1], nums[2])] = [1, 2, 1]</code>.</p>

<p>升序排序后得到&nbsp;<code>gcdPairs = [1, 1, 2]</code>&nbsp;。</p>

<p>所以答案为&nbsp;<code>[gcdPairs[queries[0]], gcdPairs[queries[1]], gcdPairs[queries[2]]] = [1, 2, 2]</code>&nbsp;。</p>
</div>

<p><strong class="example">示例 2：</strong></p>

<div class="example-block">
<p><span class="example-io"><b>输入：</b>nums = [4,4,2,1], queries = [5,3,1,0]</span></p>

<p><span class="example-io"><b>输出：</b>[4,2,1,1]</span></p>

<p><strong>解释：</strong></p>

<p><code>gcdPairs</code>&nbsp;升序排序后得到&nbsp;<code>[1, 1, 1, 2, 2, 4]</code>&nbsp;。</p>
</div>

<p><strong class="example">示例 3：</strong></p>

<div class="example-block">
<p><span class="example-io"><b>输入：</b>nums = [2,2], queries = [0,0]</span></p>

<p><span class="example-io"><b>输出：</b>[2,2]</span></p>

<p><b>解释：</b></p>

<p><code>gcdPairs = [2]</code>&nbsp;。</p>
</div>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>2 &lt;= n == nums.length &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= nums[i] &lt;= 5 * 10<sup>4</sup></code></li>
	<li><code>1 &lt;= queries.length &lt;= 10<sup>5</sup></code></li>
	<li><code>0 &lt;= queries[i] &lt; n * (n - 1) / 2</code></li>
</ul>
