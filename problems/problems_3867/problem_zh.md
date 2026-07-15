# 3867. 数对的最大公约数之和 [难度分: 1406.63]

<p>给你一个长度为 <code>n</code> 的整数数组 <code>nums</code>。</p>


<p>构造一个数组 <code>prefixGcd</code>，其中对于每个下标&nbsp;<code>i</code>：</p>

<ul>
	<li>令 <code>mx<sub>i</sub> = max(nums[0], nums[1], ..., nums[i])</code>。</li>
	<li><code>prefixGcd[i] = gcd(nums[i], mx<sub>i</sub>)</code>。</li>
</ul>

<p>在构造 <code>prefixGcd</code> 之后：</p>

<ul>
	<li>将 <code>prefixGcd</code> 按 <strong>非递减</strong> 顺序排序。</li>
	<li>通过取 <strong>最小的未配对</strong> 元素和 <strong>最大的未配对</strong> 元素来形成数对。</li>
	<li>重复此过程，直到无法再形成更多数对。</li>
	<li>对于每个形成的数对，<strong>计算</strong> 两个元素的最大公约数&nbsp;<code>gcd</code>。</li>
	<li>如果 <code>n</code> 是奇数，<code>prefixGcd</code> 数组中的 <strong>中间</strong> 元素保持 <strong>未配对</strong> 状态，并应被忽略。</li>
</ul>

<p>返回一个整数，表示所有形成数对的 <strong>最大公约数之和</strong>。</p>
术语 <code>gcd(a, b)</code> 表示 <code>a</code> 和 <code>b</code> 的 <strong>最大公约数</strong>。

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>

<div class="example-block">
<p><strong>输入：</strong> <span class="example-io">nums = [2,6,4]</span></p>

<p><strong>输出：</strong> <span class="example-io">2</span></p>

<p><strong>解释：</strong></p>

<p>构造 <code>prefixGcd</code>：</p>

<table style="border: 1px solid black;">
	<thead>
		<tr>
			<th style="border: 1px solid black;"><code>i</code></th>
			<th style="border: 1px solid black;"><code>nums[i]</code></th>
			<th style="border: 1px solid black;"><code>mx<sub>i</sub></code></th>
			<th style="border: 1px solid black;"><code>prefixGcd[i]</code></th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td style="border: 1px solid black;">0</td>
			<td style="border: 1px solid black;">2</td>
			<td style="border: 1px solid black;">2</td>
			<td style="border: 1px solid black;">2</td>
		</tr>
		<tr>
			<td style="border: 1px solid black;">1</td>
			<td style="border: 1px solid black;">6</td>
			<td style="border: 1px solid black;">6</td>
			<td style="border: 1px solid black;">6</td>
		</tr>
		<tr>
			<td style="border: 1px solid black;">2</td>
			<td style="border: 1px solid black;">4</td>
			<td style="border: 1px solid black;">6</td>
			<td style="border: 1px solid black;">2</td>
		</tr>
	</tbody>
</table>

<p><code>prefixGcd = [2, 6, 2]</code>。排序后形成 <code>[2, 2, 6]</code>。</p>

<p>将最小和最大的元素配对：<code>gcd(2, 6) = 2</code>。剩下的中间元素 2 被忽略。因此，总和为 2。</p>
</div>

<p><strong class="example">示例 2：</strong></p>

<div class="example-block">
<p><strong>输入：</strong> <span class="example-io">nums = [3,6,2,8]</span></p>

<p><strong>输出：</strong> <span class="example-io">5</span></p>

<p><strong>解释：</strong></p>

<p>构造 <code>prefixGcd</code>：</p>

<table style="border: 1px solid black;">
	<thead>
		<tr>
			<th style="border: 1px solid black;"><code>i</code></th>
			<th style="border: 1px solid black;"><code>nums[i]</code></th>
			<th style="border: 1px solid black;"><code>mx<sub>i</sub></code></th>
			<th style="border: 1px solid black;"><code>prefixGcd[i]</code></th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td style="border: 1px solid black;">0</td>
			<td style="border: 1px solid black;">3</td>
			<td style="border: 1px solid black;">3</td>
			<td style="border: 1px solid black;">3</td>
		</tr>
		<tr>
			<td style="border: 1px solid black;">1</td>
			<td style="border: 1px solid black;">6</td>
			<td style="border: 1px solid black;">6</td>
			<td style="border: 1px solid black;">6</td>
		</tr>
		<tr>
			<td style="border: 1px solid black;">2</td>
			<td style="border: 1px solid black;">2</td>
			<td style="border: 1px solid black;">6</td>
			<td style="border: 1px solid black;">2</td>
		</tr>
		<tr>
			<td style="border: 1px solid black;">3</td>
			<td style="border: 1px solid black;">8</td>
			<td style="border: 1px solid black;">8</td>
			<td style="border: 1px solid black;">8</td>
		</tr>
	</tbody>
</table>

<p><code>prefixGcd = [3, 6, 2, 8]</code>。排序后形成 <code>[2, 3, 6, 8]</code>。</p>

<p>形成数对：<code>gcd(2, 8) = 2</code> 和 <code>gcd(3, 6) = 3</code>。因此，总和为 <code>2 + 3 = 5</code>。</p>
</div>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= n == nums.length &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= nums[i] &lt;= 10<sup>9</sup></code></li>
</ul>
