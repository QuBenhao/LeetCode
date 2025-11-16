# 1437. 是否所有 1 都至少相隔 k 个元素 [难度分: 1193.27]

<p>给你一个由若干 <code>0</code> 和 <code>1</code> 组成的数组 <code>nums</code> 以及整数 <code>k</code>。如果所有 <code>1</code> 都至少相隔 <code>k</code> 个元素，则返回 <font color="#c7254e" face="Menlo, Monaco, Consolas, Courier New, monospace"><span style="font-size: 12.6px; background-color: rgb(249, 242, 244);">true</span></font>&nbsp;；否则，返回 <code>false</code> 。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<p><strong><img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2020/05/03/sample_1_1791.png" style="width: 214px;" /></strong></p>

<pre>
<strong>输入：</strong>nums = [1,0,0,0,1,0,0,1], k = 2
<strong>输出：</strong>true
<strong>解释：</strong>每个 1 都至少相隔 2 个元素。</pre>

<p><strong>示例 2：</strong></p>

<p><strong><img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2020/05/03/sample_2_1791.png" style="height: 86px; width: 160px;" /></strong></p>

<pre>
<strong>输入：</strong>nums = [1,0,0,1,0,1], k = 2
<strong>输出：</strong>false
<strong>解释：</strong>第二个 1 和第三个 1 之间只隔了 1 个元素。</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 10<sup>5</sup></code></li>
	<li><code>0 &lt;= k &lt;= nums.length</code></li>
	<li><code>nums[i]</code> 的值为 <code>0</code> 或 <code>1</code></li>
</ul>
