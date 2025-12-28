# 3788. 分割的最大得分 

<p>给你一个长度为 <code>n</code> 的整数数组 <code>nums</code>。</p>

<p>请你选出一个下标 <code>i</code>&nbsp;以分割数组，该下标满足 <code>0 &lt;= i &lt; n - 1</code>。</p>

<p>对于选择的分割下标 <code>i</code>：</p>

<ul>
	<li>令 <code>prefixSum(i)</code> 表示数组前缀的和，即 <code>nums[0] + nums[1] + ... + nums[i]</code>。</li>
	<li>令 <code>suffixMin(i)</code> 表示数组后缀的最小值，即 <code>nums[i + 1], nums[i + 2], ..., nums[n - 1]</code> 中的最小值。</li>
</ul>

<p>在下标 <code>i</code> 的<strong>&nbsp;分割得分</strong>&nbsp;定义为：</p>

<p><code>score(i) = prefixSum(i) - suffixMin(i)</code></p>

<p>返回所有有效分割下标中&nbsp;<strong>最大</strong>&nbsp;的分割得分。</p>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>

<div class="example-block">
<p><strong>输入：</strong> <span class="example-io">nums = [10,-1,3,-4,-5]</span></p>

<p><strong>输出：</strong> <span class="example-io">17</span></p>

<p><strong>解释：</strong></p>

<p>最优的分割下标是 <code>i = 2</code>，<code>score(2) = prefixSum(2) - suffixMin(2) = (10 + (-1) + 3) - (-5) = 17</code>。</p>
</div>

<p><strong class="example">示例 2：</strong></p>

<div class="example-block">
<p><strong>输入：</strong> <span class="example-io">nums = [-7,-5,3]</span></p>

<p><strong>输出：</strong> <span class="example-io">-2</span></p>

<p><strong>解释：</strong></p>

<p>最优的分割下标是 <code>i = 0</code>，<code>score(0) = prefixSum(0) - suffixMin(0) = (-7) - (-5) = -2</code>。</p>
</div>

<p><strong class="example">示例 3：</strong></p>

<div class="example-block">
<p><strong>输入：</strong> <span class="example-io">nums = [1,1]</span></p>

<p><strong>输出：</strong> <span class="example-io">0</span></p>

<p><strong>解释：</strong></p>

<p>唯一有效分割下标是 <code>i = 0</code>，<code>score(0) = prefixSum(0) - suffixMin(0) = 1 - 1 = 0</code>。</p>
</div>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>2 &lt;= nums.length &lt;= 10<sup>5</sup></code></li>
	<li><code>-10<sup>9</sup>​​​​​​​ &lt;= nums[i] &lt;= 10<sup>9</sup></code></li>
</ul>
