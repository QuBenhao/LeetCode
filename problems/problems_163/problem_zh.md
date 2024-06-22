# 163. 缺失的区间

<p>给你一个闭区间&nbsp;<code>[lower, upper]</code> 和一个 <strong>按从小到大排序</strong> 的整数数组 <code>nums</code><em><strong>&nbsp;</strong></em>，其中元素的范围在闭区间&nbsp;<code>[lower, upper]</code>&nbsp;当中。</p>

<p>如果一个数字 <code>x</code> 在 <code>[lower, upper]</code>&nbsp;区间内，并且 <code>x</code> 不在 <code>nums</code> 中，则认为 <code>x</code> <strong>缺失</strong>。</p>

<p>返回&nbsp;<strong>准确涵盖所有缺失数字&nbsp;</strong>的 <strong>最小排序</strong> 区间列表。也就是说，<code>nums</code> 的任何元素都不在任何区间内，并且每个缺失的数字都在其中一个区间内。</p>
&nbsp;

<p><strong class="example">示例 1：</strong></p>

<pre>
<strong>输入: </strong>nums = <code>[0, 1, 3, 50, 75]</code>, lower = 0 , upper = 99
<strong>输出: </strong>[[2,2],[4,49],[51,74],[76,99]]
<strong>解释：</strong>返回的区间是：
[2,2]
[4,49]
[51,74]
[76,99]</pre>

<p><strong class="example">示例 2：</strong></p>

<pre>
<strong>输入：</strong> nums = [-1], lower = -1, upper = -1
<strong>输出：</strong> []
<b>解释：</b>&nbsp;没有缺失的区间，因为没有缺失的数字。</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>-10<sup>9</sup> &lt;= lower &lt;= upper &lt;= 10<sup>9</sup></code></li>
	<li><code>0 &lt;= nums.length &lt;= 100</code></li>
	<li><code>lower &lt;= nums[i] &lt;= upper</code></li>
	<li><code>nums</code> 中的所有值 <strong>互不相同</strong></li>
</ul>
