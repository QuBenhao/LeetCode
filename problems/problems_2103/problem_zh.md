# 2103. 环和杆 [难度分: 1257.77]

<p>总计有 <code>n</code> 个环，环的颜色可以是红、绿、蓝中的一种。这些环分别穿在 10 根编号为 <code>0</code> 到 <code>9</code> 的杆上。</p>

<p>给你一个长度为 <code>2n</code> 的字符串 <code>rings</code> ，表示这 <code>n</code> 个环在杆上的分布。<code>rings</code> 中每两个字符形成一个 <strong>颜色位置对</strong> ，用于描述每个环：</p>

<ul>
	<li>第 <code>i</code> 对中的 <strong>第一个</strong> 字符表示第 <code>i</code> 个环的 <strong>颜色</strong>（<code>'R'</code>、<code>'G'</code>、<code>'B'</code>）。</li>
	<li>第 <code>i</code> 对中的 <strong>第二个</strong> 字符表示第 <code>i</code> 个环的 <strong>位置</strong>，也就是位于哪根杆上（<code>'0'</code> 到 <code>'9'</code>）。</li>
</ul>

<p>例如，<code>"R3G2B1"</code> 表示：共有 <code>n == 3</code> 个环，红色的环在编号为 3 的杆上，绿色的环在编号为 2 的杆上，蓝色的环在编号为 1 的杆上。</p>

<p>找出所有集齐 <strong>全部三种颜色</strong> 环的杆，并返回这种杆的数量。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/11/23/ex1final.png" style="width: 258px; height: 130px;" />
<pre>
<strong>输入：</strong>rings = "B0B6G0R6R0R6G9"
<strong>输出：</strong>1
<strong>解释：</strong>
- 编号 0 的杆上有 3 个环，集齐全部颜色：红、绿、蓝。
- 编号 6 的杆上有 3 个环，但只有红、蓝两种颜色。
- 编号 9 的杆上只有 1 个绿色环。
因此，集齐全部三种颜色环的杆的数目为 1 。
</pre>

<p><strong>示例 2：</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/11/23/ex2final.png" style="width: 266px; height: 130px;" />
<pre>
<strong>输入：</strong>rings = "B0R0G0R9R0B0G0"
<strong>输出：</strong>1
<strong>解释：</strong>
- 编号 0 的杆上有 6 个环，集齐全部颜色：红、绿、蓝。
- 编号 9 的杆上只有 1 个红色环。
因此，集齐全部三种颜色环的杆的数目为 1 。
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>rings = "G4"
<strong>输出：</strong>0
<strong>解释：</strong>
只给了一个环，因此，不存在集齐全部三种颜色环的杆。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>rings.length == 2 * n</code></li>
	<li><code>1 &lt;= n &lt;= 100</code></li>
	<li>如 <code>i</code> 是 <strong>偶数</strong> ，则&nbsp;<code>rings[i]</code> 的值可以取 <code>'R'</code>、<code>'G'</code> 或 <code>'B'</code>（下标从 <strong>0</strong> 开始计数）</li>
	<li>如 <code>i</code> 是 <strong>奇数</strong> ，则&nbsp;<code>rings[i]</code> 的值可以取 <code>'0'</code> 到 <code>'9'</code> 中的一个数字（下标从 <strong>0</strong> 开始计数）</li>
</ul>
