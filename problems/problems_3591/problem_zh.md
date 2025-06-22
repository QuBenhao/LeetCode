# 3591. 检查元素频次是否为质数 

<p>给你一个整数数组 <code>nums</code>。</p>

<p>如果数组中任一元素的&nbsp;<strong>频次&nbsp;</strong>是&nbsp;<strong>质数</strong>，返回 <code>true</code>；否则，返回 <code>false</code>。</p>

<p>元素 <code>x</code> 的&nbsp;<strong>频次&nbsp;</strong>是它在数组中出现的次数。</p>

<p>质数是一个大于 1 的自然数，并且只有两个因数：1 和它本身。</p>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>

<div class="example-block">
<p><strong>输入：</strong> <span class="example-io">nums = [1,2,3,4,5,4]</span></p>

<p><strong>输出：</strong> <span class="example-io">true</span></p>

<p><strong>解释：</strong></p>

<p>数字 4 的频次是 2，而 2 是质数。</p>
</div>

<p><strong class="example">示例 2：</strong></p>

<div class="example-block">
<p><strong>输入：</strong> <span class="example-io">nums = [1,2,3,4,5]</span></p>

<p><strong>输出：</strong> <span class="example-io">false</span></p>

<p><strong>解释：</strong></p>

<p>所有元素的频次都是 1。</p>
</div>

<p><strong class="example">示例 3：</strong></p>

<div class="example-block">
<p><strong>输入：</strong> <span class="example-io">nums = [2,2,2,4,4]</span></p>

<p><strong>输出：</strong> <span class="example-io">true</span></p>

<p><strong>解释：</strong></p>

<p>数字 2 和 4 的频次都是质数。</p>
</div>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 100</code></li>
	<li><code>0 &lt;= nums[i] &lt;= 100</code></li>
</ul>
