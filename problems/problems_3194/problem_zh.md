# 3194. 最小元素和最大元素的最小平均值 [难度分: 1194.63]

<p>你有一个初始为空的浮点数数组 <code>averages</code>。另给你一个包含 <code>n</code> 个整数的数组 <code>nums</code>，其中 <code>n</code> 为偶数。</p>

<p>你需要重复以下步骤 <code>n / 2</code> 次：</p>

<ul>
	<li>从 <code>nums</code> 中移除<strong> 最小 </strong>的元素 <code>minElement</code> 和<strong> 最大 </strong>的元素 <code>maxElement</code>。</li>
	<li>将 <code>(minElement + maxElement) / 2</code> 加入到 <code>averages</code> 中。</li>
</ul>

<p>返回 <code>averages</code> 中的 <strong>最小 </strong>元素。</p>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>

<div class="example-block">
<p><strong>输入：</strong> <span class="example-io">nums = [7,8,3,4,15,13,4,1]</span></p>

<p><strong>输出：</strong> <span class="example-io">5.5</span></p>

<p><strong>解释：</strong></p>

<table>
	<tbody>
		<tr>
			<th>步骤</th>
			<th>nums</th>
			<th>averages</th>
		</tr>
		<tr>
			<td>0</td>
			<td>[7,8,3,4,15,13,4,1]</td>
			<td>[]</td>
		</tr>
		<tr>
			<td>1</td>
			<td>[7,8,3,4,13,4]</td>
			<td>[8]</td>
		</tr>
		<tr>
			<td>2</td>
			<td>[7,8,4,4]</td>
			<td>[8,8]</td>
		</tr>
		<tr>
			<td>3</td>
			<td>[7,4]</td>
			<td>[8,8,6]</td>
		</tr>
		<tr>
			<td>4</td>
			<td>[]</td>
			<td>[8,8,6,5.5]</td>
		</tr>
	</tbody>
</table>
返回 averages 中最小的元素，即 5.5。</div>

<p><strong class="example">示例 2：</strong></p>

<div class="example-block">
<p><strong>输入：</strong> <span class="example-io">nums = [1,9,8,3,10,5]</span></p>

<p><strong>输出：</strong> <span class="example-io">5.5</span></p>

<p><strong>解释：</strong></p>

<table>
	<tbody>
		<tr>
			<th>步骤</th>
			<th>nums</th>
			<th>averages</th>
		</tr>
		<tr>
			<td>0</td>
			<td>[1,9,8,3,10,5]</td>
			<td>[]</td>
		</tr>
		<tr>
			<td>1</td>
			<td>[9,8,3,5]</td>
			<td>[5.5]</td>
		</tr>
		<tr>
			<td>2</td>
			<td>[8,5]</td>
			<td>[5.5,6]</td>
		</tr>
		<tr>
			<td>3</td>
			<td>[]</td>
			<td>[5.5,6,6.5]</td>
		</tr>
	</tbody>
</table>
</div>

<p><strong class="example">示例 3：</strong></p>

<div class="example-block">
<p><strong>输入：</strong> <span class="example-io">nums = [1,2,3,7,8,9]</span></p>

<p><strong>输出：</strong> <span class="example-io">5.0</span></p>

<p><strong>解释：</strong></p>

<table>
	<tbody>
		<tr>
			<th>步骤</th>
			<th>nums</th>
			<th>averages</th>
		</tr>
		<tr>
			<td>0</td>
			<td>[1,2,3,7,8,9]</td>
			<td>[]</td>
		</tr>
		<tr>
			<td>1</td>
			<td>[2,3,7,8]</td>
			<td>[5]</td>
		</tr>
		<tr>
			<td>2</td>
			<td>[3,7]</td>
			<td>[5,5]</td>
		</tr>
		<tr>
			<td>3</td>
			<td>[]</td>
			<td>[5,5,5]</td>
		</tr>
	</tbody>
</table>
</div>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>2 &lt;= n == nums.length &lt;= 50</code></li>
	<li><code>n</code> 为偶数。</li>
	<li><code>1 &lt;= nums[i] &lt;= 50</code></li>
</ul>
