# 2402. 会议室 III [难度分: 2092.89]

<p>给你一个整数 <code>n</code> ，共有编号从 <code>0</code> 到 <code>n - 1</code> 的 <code>n</code> 个会议室。</p>

<p>给你一个二维整数数组 <code>meetings</code> ，其中 <code>meetings[i] = [start<sub>i</sub>, end<sub>i</sub>]</code> 表示一场会议将会在 <strong>半闭</strong> 时间区间 <code>[start<sub>i</sub>, end<sub>i</sub>)</code> 举办。所有 <code>start<sub>i</sub></code> 的值 <strong>互不相同</strong> 。</p>

<p>会议将会按以下方式分配给会议室：</p>

<ol>
	<li>每场会议都会在未占用且编号 <strong>最小</strong> 的会议室举办。</li>
	<li>如果没有可用的会议室，会议将会延期，直到存在空闲的会议室。延期会议的持续时间和原会议持续时间 <strong>相同</strong> 。</li>
	<li>当会议室处于未占用状态时，将会优先提供给原 <strong>开始</strong> 时间更早的会议。</li>
</ol>

<p>返回举办最多次会议的房间 <strong>编号</strong> 。如果存在多个房间满足此条件，则返回编号 <strong>最小</strong> 的房间。</p>

<p><strong>半闭区间 </strong><code>[a, b)</code> 是 <code>a</code> 和 <code>b</code> 之间的区间，<strong>包括</strong> <code>a</code> 但<strong> 不包括</strong> <code>b</code> 。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre><strong>输入：</strong>n = 2, meetings = [[0,10],[1,5],[2,7],[3,4]]
<strong>输出：</strong>0
<strong>解释：</strong>
- 在时间 0 ，两个会议室都未占用，第一场会议在会议室 0 举办。
- 在时间 1 ，只有会议室 1 未占用，第二场会议在会议室 1 举办。
- 在时间 2 ，两个会议室都被占用，第三场会议延期举办。
- 在时间 3 ，两个会议室都被占用，第四场会议延期举办。
- 在时间 5 ，会议室 1 的会议结束。第三场会议在会议室 1 举办，时间周期为 [5,10) 。
- 在时间 10 ，两个会议室的会议都结束。第四场会议在会议室 0 举办，时间周期为 [10,11) 。
会议室 0 和会议室 1 都举办了 2 场会议，所以返回 0 。 
</pre>

<p><strong>示例 2：</strong></p>

<pre><strong>输入：</strong>n = 3, meetings = [[1,20],[2,10],[3,5],[4,9],[6,8]]
<strong>输出：</strong>1
<strong>解释：</strong>
- 在时间 1 ，所有三个会议室都未占用，第一场会议在会议室 0 举办。
- 在时间 2 ，会议室 1 和 2 未占用，第二场会议在会议室 1 举办。
- 在时间 3 ，只有会议室 2 未占用，第三场会议在会议室 2 举办。
- 在时间 4 ，所有三个会议室都被占用，第四场会议延期举办。 
- 在时间 5 ，会议室 2 的会议结束。第四场会议在会议室 2 举办，时间周期为 [5,10) 。
- 在时间 6 ，所有三个会议室都被占用，第五场会议延期举办。 
- 在时间 10 ，会议室 1 和 2 的会议结束。第五场会议在会议室 1 举办，时间周期为 [10,12) 。 
会议室 1 和会议室 2 都举办了 2 场会议，所以返回 1 。 
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= n &lt;= 100</code></li>
	<li><code>1 &lt;= meetings.length &lt;= 10<sup>5</sup></code></li>
	<li><code>meetings[i].length == 2</code></li>
	<li><code>0 &lt;= start<sub>i</sub> &lt; end<sub>i</sub> &lt;= 5 * 10<sup>5</sup></code></li>
	<li><code>start<sub>i</sub></code> 的所有值 <strong>互不相同</strong></li>
</ul>
