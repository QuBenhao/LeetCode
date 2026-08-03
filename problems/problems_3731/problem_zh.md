# 3731. 找出缺失的元素 [难度分: 1217.11]

<p>给你一个整数数组 <code>nums</code> ，数组由若干&nbsp;<b>互不相同</b> 的整数组成。</p>

<p>数组 <code>nums</code> 原本包含了某个范围内的&nbsp;<strong>所有整数&nbsp;</strong>。但现在，其中可能 <strong>缺失</strong> 部分整数。</p>

<p>该范围内的&nbsp;<strong>最小&nbsp;</strong>整数和&nbsp;<strong>最大&nbsp;</strong>整数仍然存在于 <code>nums</code> 中。</p>

<p>返回一个&nbsp;<strong>有序&nbsp;</strong>列表，包含该范围内缺失的所有整数，并&nbsp;<strong>按从小到大排序</strong>。如果没有缺失的整数，返回一个&nbsp;<strong>空&nbsp;</strong>列表。</p>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>

<div class="example-block">
<p><strong>输入：</strong> <span class="example-io">nums = [1,4,2,5]</span></p>

<p><strong>输出：</strong> <span class="example-io">[3]</span></p>

<p><strong>解释：</strong></p>

<p>最小整数为 1，最大整数为 5，因此完整的范围应为 <code>[1,2,3,4,5]</code>。其中只有 3 缺失。</p>
</div>

<p><strong class="example">示例 2：</strong></p>

<div class="example-block">
<p><strong>输入：</strong> <span class="example-io">nums = [7,8,6,9]</span></p>

<p><strong>输出：</strong> <span class="example-io">[]</span></p>

<p><strong>解释：</strong></p>

<p>最小整数为 6，最大整数为 9，因此完整的范围为 <code>[6,7,8,9]</code>。所有整数均已存在，因此没有缺失的整数。</p>
</div>

<p><strong class="example">示例 3：</strong></p>

<div class="example-block">
<p><strong>输入：</strong> <span class="example-io">nums = [5,1]</span></p>

<p><strong>输出：</strong> <span class="example-io">[2,3,4]</span></p>

<p><strong>解释：</strong></p>

<p>最小整数为 1，最大整数为 5，因此完整的范围应为 <code>[1,2,3,4,5]</code>。缺失的整数为 2、3 和 4。</p>
</div>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>2 &lt;= nums.length &lt;= 100</code></li>
	<li><code>1 &lt;= nums[i] &lt;= 100</code></li>
</ul>
