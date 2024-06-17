# 57. 插入区间

<p>给你一个<strong> 无重叠的</strong><em> ，</em>按照区间起始端点排序的区间列表 <code>intervals</code>，其中&nbsp;<code>intervals[i] = [start<sub>i</sub>, end<sub>i</sub>]</code>&nbsp;表示第&nbsp;<code>i</code>&nbsp;个区间的开始和结束，并且&nbsp;<code>intervals</code>&nbsp;按照&nbsp;<code>start<sub>i</sub></code>&nbsp;升序排列。同样给定一个区间&nbsp;<code>newInterval = [start, end]</code>&nbsp;表示另一个区间的开始和结束。</p>

<p>在&nbsp;<code>intervals</code> 中插入区间&nbsp;<code>newInterval</code>，使得&nbsp;<code>intervals</code>&nbsp;依然按照&nbsp;<code>start<sub>i</sub></code>&nbsp;升序排列，且区间之间不重叠（如果有必要的话，可以合并区间）。</p>

<p>返回插入之后的&nbsp;<code>intervals</code>。</p>

<p><strong>注意</strong> 你不需要原地修改&nbsp;<code>intervals</code>。你可以创建一个新数组然后返回它。</p>

<p>&nbsp;</p>

<p><strong>示例&nbsp;1：</strong></p>

<pre>
<strong>输入：</strong>intervals = [[1,3],[6,9]], newInterval = [2,5]
<strong>输出：</strong>[[1,5],[6,9]]
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
<strong>输出：</strong>[[1,2],[3,10],[12,16]]
<strong>解释：</strong>这是因为新的区间 <code>[4,8]</code> 与 <code>[3,5],[6,7],[8,10]</code>&nbsp;重叠。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>0 &lt;= intervals.length &lt;= 10<sup>4</sup></code></li>
	<li><code>intervals[i].length == 2</code></li>
	<li><code>0 &lt;=&nbsp;start<sub>i</sub> &lt;=&nbsp;end<sub>i</sub> &lt;= 10<sup>5</sup></code></li>
	<li><code>intervals</code> 根据 <code>start<sub>i</sub></code> 按 <strong>升序</strong> 排列</li>
	<li><code>newInterval.length == 2</code></li>
	<li><code>0 &lt;=&nbsp;start &lt;=&nbsp;end &lt;= 10<sup>5</sup></code></li>
</ul>
