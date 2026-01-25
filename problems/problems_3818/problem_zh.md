# 3818. 移除前缀使数组严格递增 

<p>给你一个整数数组 <code>nums</code>。</p>

<p>你需要从 <code>nums</code> 中<strong>&nbsp;恰好&nbsp;</strong>移除一个前缀（可以为空）。</p>

<p>返回一个整数，表示被移除的前缀的<strong>&nbsp;最小</strong>&nbsp;长度，使得剩余的数组 <strong>严格递增</strong>&nbsp;。</p>

<p>数组的<strong>&nbsp;前缀&nbsp;</strong>是从数组的起始位置开始，一直延伸到任意位置的子数组。</p>

<p>如果一个数组的每个元素都严格大于它的前一个元素（若存在），则称该数组<strong>&nbsp;严格递增</strong>&nbsp;。</p>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>

<div class="example-block">
<p><strong>输入：</strong> <span class="example-io">nums = [1,-1,2,3,3,4,5]</span></p>

<p><strong>输出：</strong> <span class="example-io">4</span></p>

<p><strong>解释：</strong></p>

<p>移除前缀 <code>prefix = [1, -1, 2, 3]</code> 后，剩余数组为 <code>[3, 4, 5]</code>，严格递增。</p>
</div>

<p><strong class="example">示例 2：</strong></p>

<div class="example-block">
<p><strong>输入：</strong> <span class="example-io">nums = [4,3,-2,-5]</span></p>

<p><strong>输出：</strong> <span class="example-io">3</span></p>

<p><strong>解释：</strong></p>

<p>移除前缀 <code>prefix = [4, 3, -2]</code> 后，剩余数组为 <code>[-5]</code>，严格递增。</p>
</div>

<p><strong class="example">示例 3：</strong></p>

<div class="example-block">
<p><strong>输入：</strong> <span class="example-io">nums = [1,2,3,4]</span></p>

<p><strong>输出：</strong> <span class="example-io">0</span></p>

<p><strong>解释：</strong></p>

<p>数组 <code>nums = [1, 2, 3, 4]</code> 已经是严格递增的，因此移除空前缀即可。</p>
</div>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 10<sup>5</sup></code></li>
	<li><code>-10<sup>9</sup> &lt;= nums[i] &lt;= 10<sup>9</sup>​​​​​​​</code></li>
</ul>
