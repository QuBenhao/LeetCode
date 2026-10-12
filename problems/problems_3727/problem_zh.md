# 3727. 最大交替平方和 [难度分: 1454.93]

<p>给你一个整数数组 <code>nums</code>。你可以以任意顺序&nbsp;<strong>重新排列元素&nbsp;</strong>。</p>

<p>数组 <code>arr</code> 的&nbsp;<strong>交替得分&nbsp;</strong>定义为：</p>

<ul>
	<li><code>score = arr[0]<sup>2</sup> - arr[1]<sup>2</sup> + arr[2]<sup>2</sup> - arr[3]<sup>2</sup> + ...</code></li>
</ul>

<p>在对 <code>nums</code> 重新排列后，返回其&nbsp;<strong>最大可能的交替得分</strong>。</p>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>

<div class="example-block">
<p><strong>输入：</strong> <span class="example-io">nums = [1,2,3]</span></p>

<p><strong>输出：</strong> <span class="example-io">12</span></p>

<p><strong>解释：</strong></p>

<p><code>nums</code> 的一种可行重排为 <code>[2,1,3]</code>，该排列在所有可能重排中给出了最大交替得分。</p>

<p>交替得分计算如下：</p>

<p><code>score = 2<sup>2</sup> - 1<sup>2</sup> + 3<sup>2</sup> = 4 - 1 + 9 = 12</code></p>
</div>

<p><strong class="example">示例 2：</strong></p>

<div class="example-block">
<p><strong>输入：</strong> <span class="example-io">nums = [1,-1,2,-2,3,-3]</span></p>

<p><strong>输出：</strong> <span class="example-io">16</span></p>

<p><strong>解释：</strong></p>

<p><code>nums</code> 的一种可行重排为 <code>[-3,-1,-2,1,3,2]</code>，该排列在所有可能重排中给出了最大交替得分。</p>

<p>交替得分计算如下：</p>

<p><code>score = (-3)<sup>2</sup> - (-1)<sup>2</sup> + (-2)<sup>2</sup> - (1)<sup>2</sup> + (3)<sup>2</sup> - (2)<sup>2</sup> = 9 - 1 + 4 - 1 + 9 - 4 = 16</code></p>
</div>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 10<sup>5</sup></code></li>
	<li><code>-4 * 10<sup>4</sup> &lt;= nums[i] &lt;= 4 * 10<sup>4</sup></code></li>
</ul>
