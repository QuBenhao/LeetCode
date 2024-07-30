# 699. 掉落的方块

<p>在二维平面上的 x 轴上，放置着一些方块。</p>

<p>给你一个二维整数数组 <code>positions</code> ，其中 <code>positions[i] = [left<sub>i</sub>, sideLength<sub>i</sub>]</code> 表示：第 <code>i</code> 个方块边长为 <code>sideLength<sub>i</sub></code> ，其左侧边与 x 轴上坐标点&nbsp;<code>left<sub>i</sub></code> 对齐。</p>

<p>每个方块都从一个比目前所有的落地方块更高的高度掉落而下。方块沿 y 轴负方向下落，直到着陆到 <strong>另一个正方形的顶边</strong> 或者是 <strong>x 轴上</strong> 。一个方块仅仅是擦过另一个方块的左侧边或右侧边不算着陆。一旦着陆，它就会固定在原地，无法移动。</p>

<p>在每个方块掉落后，你必须记录目前所有已经落稳的 <strong>方块堆叠的最高高度</strong> 。</p>

<p>返回一个整数数组 <code>ans</code> ，其中 <code>ans[i]</code> 表示在第 <code>i</code> 块方块掉落后堆叠的最高高度。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/04/28/fallingsq1-plane.jpg" style="width: 500px; height: 505px;" />
<pre>
<strong>输入：</strong>positions = [[1,2],[2,3],[6,1]]
<strong>输出：</strong>[2,5,5]
<strong>解释：</strong>
第 1 个方块掉落后，最高的堆叠由方块 1 组成，堆叠的最高高度为 2 。
第 2 个方块掉落后，最高的堆叠由方块 1 和 2 组成，堆叠的最高高度为 5 。
第 3 个方块掉落后，最高的堆叠仍然由方块 1 和 2 组成，堆叠的最高高度为 5 。
因此，返回 [2, 5, 5] 作为答案。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>positions = [[100,100],[200,100]]
<strong>输出：</strong>[100,100]
<strong>解释：</strong>
第 1 个方块掉落后，最高的堆叠由方块 1 组成，堆叠的最高高度为 100 。
第 2 个方块掉落后，最高的堆叠可以由方块 1 组成也可以由方块 2 组成，堆叠的最高高度为 100 。
因此，返回 [100, 100] 作为答案。
注意，方块 2 擦过方块 1 的右侧边，但不会算作在方块 1 上着陆。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= positions.length &lt;= 1000</code></li>
	<li><code>1 &lt;= left<sub>i</sub> &lt;= 10<sup>8</sup></code></li>
	<li><code>1 &lt;= sideLength<sub>i</sub> &lt;= 10<sup>6</sup></code></li>
</ul>
