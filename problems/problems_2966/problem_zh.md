# 2966. 划分数组并满足最大差限制 [难度分: 1395.96]

<p>给你一个长度为 <code>n</code> 的整数数组 <code>nums</code>，以及一个正整数 <code>k</code> 。</p>

<p>将这个数组划分为&nbsp;<code>n / 3</code>&nbsp;个长度为 <code>3</code> 的子数组，并满足以下条件：</p>

<ul>
	<li>子数组中<strong> 任意 </strong>两个元素的差必须 <strong>小于或等于</strong> <code>k</code> 。</li>
</ul>

<p>返回一个<em> </em><strong>二维数组 </strong>，包含所有的子数组。如果不可能满足条件，就返回一个空数组。如果有多个答案，返回 <strong>任意一个</strong> 即可。</p>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>

<div class="example-block">
<p><span class="example-io"><b>输入：</b>nums = [1,3,4,8,7,9,3,5,1], k = 2</span></p>

<p><span class="example-io"><b>输出：</b>[[1,1,3],[3,4,5],[7,8,9]]</span></p>

<p><strong>解释：</strong></p>

<p>每个数组中任何两个元素之间的差小于或等于 2。</p>
</div>

<p><strong class="example">示例 2：</strong></p>

<div class="example-block">
<p><span class="example-io"><b>输入：</b></span><span class="example-io">nums = [2,4,2,2,5,2], k = 2</span></p>

<p><span class="example-io"><b>输出：</b></span><span class="example-io">[]</span></p>

<p><strong>解释：</strong></p>

<p>将&nbsp;<code>nums</code>&nbsp;划分为 2 个长度为 3 的数组的不同方式有：</p>

<ul>
	<li>[[2,2,2],[2,4,5]] （及其排列）</li>
	<li>[[2,2,4],[2,2,5]] （及其排列）</li>
</ul>

<p>因为有四个 2，所以无论我们如何划分，都会有一个包含元素 2 和 5 的数组。因为&nbsp;<code>5 - 2 = 3 &gt; k</code>，条件无法被满足，所以没有合法的划分。</p>
</div>

<p><strong class="example">示例 3：</strong></p>

<div class="example-block">
<p><span class="example-io"><b>输入：</b></span><span class="example-io">nums = [4,2,9,8,2,12,7,12,10,5,8,5,5,7,9,2,5,11], k = 14</span></p>

<p><span class="example-io"><b>输出：</b></span><span class="example-io">[[2,2,12],[4,8,5],[5,9,7],[7,8,5],[5,9,10],[11,12,2]]</span></p>

<p><strong>解释：</strong></p>

<p>每个数组中任何两个元素之间的差小于或等于 14。</p>
</div>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>n == nums.length</code></li>
	<li><code>1 &lt;= n &lt;= 10<sup>5</sup></code></li>
	<li><code>n</code> 是 <code>3</code> 的倍数</li>
	<li><code>1 &lt;= nums[i] &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= k &lt;= 10<sup>5</sup></code></li>
</ul>
