# 731. 我的日程安排表 II 

<p>实现一个程序来存放你的日程安排。如果要添加的时间内不会导致三重预订时，则可以存储这个新的日程安排。</p>

<p>当三个日程安排有一些时间上的交叉时（例如三个日程安排都在同一时间内），就会产生 <strong>三重预订</strong>。</p>

<p>事件能够用一对整数&nbsp;<code>startTime</code>&nbsp;和&nbsp;<code>endTime</code>&nbsp;表示，在一个半开区间的时间&nbsp;<code>[startTime, endTime)</code>&nbsp;上预定。实数&nbsp;<code>x</code> 的范围为&nbsp;&nbsp;<code>startTime &lt;= x &lt; endTime</code>。</p>

<p>实现&nbsp;<code>MyCalendarTwo</code> 类：</p>

<ul>
	<li><code>MyCalendarTwo()</code>&nbsp;初始化日历对象。</li>
	<li><code>boolean book(int startTime, int endTime)</code>&nbsp;如果可以将日程安排成功添加到日历中而不会导致三重预订，返回 <code>true</code>。否则，返回 <code>false</code> 并且不要将该日程安排添加到日历中。</li>
</ul>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>

<pre>
<strong>输入：</strong>
["MyCalendarTwo", "book", "book", "book", "book", "book", "book"]
[[], [10, 20], [50, 60], [10, 40], [5, 15], [5, 10], [25, 55]]
<strong>输出：</strong>
[null, true, true, true, false, true, true]

<strong>解释：</strong>
MyCalendarTwo myCalendarTwo = new MyCalendarTwo();
myCalendarTwo.book(10, 20); // 返回 True，能够预定该日程。
myCalendarTwo.book(50, 60); // 返回 True，能够预定该日程。
myCalendarTwo.book(10, 40); // 返回 True，该日程能够被重复预定。
myCalendarTwo.book(5, 15);  // 返回 False，该日程导致了三重预定，所以不能预定。
myCalendarTwo.book(5, 10); // 返回 True，能够预定该日程，因为它不使用已经双重预订的时间 10。
myCalendarTwo.book(25, 55); // 返回 True，能够预定该日程，因为时间段 [25, 40) 将被第三个日程重复预定，时间段 [40, 50) 将被单独预定，而时间段 [50, 55) 将被第二个日程重复预定。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>0 &lt;= start &lt; end &lt;= 10<sup>9</sup></code></li>
	<li>最多调用&nbsp;<code>book</code>&nbsp;1000 次。</li>
</ul>
