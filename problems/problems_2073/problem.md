# 2073. Time Needed to Buy Tickets [Rating: 1325.36]

<p>There are <code>n</code> people in a line queuing to buy tickets, where the <code>0<sup>th</sup></code> person is at the <strong>front</strong> of the line and the <code>(n - 1)<sup>th</sup></code> person is at the <strong>back</strong> of the line.</p>

<p>You are given a <strong>0-indexed</strong> integer array <code>tickets</code> of length <code>n</code> where the number of tickets that the <code>i<sup>th</sup></code> person would like to buy is <code>tickets[i]</code>.</p>

<p>Each person takes <strong>exactly 1 second</strong> to buy a ticket. A person can only buy <strong>1 ticket at a time</strong> and has to go back to <strong>the end</strong> of the line (which happens <strong>instantaneously</strong>) in order to buy more tickets. If a person does not have any tickets left to buy, the person will <strong>leave </strong>the line.</p>

<p>Return the <strong>time taken</strong> for the person <strong>initially</strong> at position <strong>k</strong><strong> </strong>(0-indexed) to finish buying tickets.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">tickets = [2,3,2], k = 2</span></p>

<p><strong>Output:</strong> <span class="example-io">6</span></p>

<p><strong>Explanation:</strong></p>

<ul>
	<li>The queue starts as [2,3,<u>2</u>], where the kth person is underlined.</li>
	<li>After the person at the front has bought a ticket, the queue becomes [3,<u>2</u>,1] at 1 second.</li>
	<li>Continuing this process, the queue becomes [<u>2</u>,1,2] at 2 seconds.</li>
	<li>Continuing this process, the queue becomes [1,2,<u>1</u>] at 3 seconds.</li>
	<li>Continuing this process, the queue becomes [2,<u>1</u>] at 4 seconds. Note: the person at the front left the queue.</li>
	<li>Continuing this process, the queue becomes [<u>1</u>,1] at 5 seconds.</li>
	<li>Continuing this process, the queue becomes [1] at 6 seconds. The kth person has bought all their tickets, so return 6.</li>
</ul>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">tickets = [5,1,1,1], k = 0</span></p>

<p><strong>Output:</strong> <span class="example-io">8</span></p>

<p><strong>Explanation:</strong></p>

<ul>
	<li>The queue starts as [<u>5</u>,1,1,1], where the kth person is underlined.</li>
	<li>After the person at the front has bought a ticket, the queue becomes [1,1,1,<u>4</u>] at 1 second.</li>
	<li>Continuing this process for 3 seconds, the queue becomes [<u>4]</u> at 4 seconds.</li>
	<li>Continuing this process for 4 seconds, the queue becomes [] at 8 seconds. The kth person has bought all their tickets, so return 8.</li>
</ul>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>n == tickets.length</code></li>
	<li><code>1 &lt;= n &lt;= 100</code></li>
	<li><code>1 &lt;= tickets[i] &lt;= 100</code></li>
	<li><code>0 &lt;= k &lt; n</code></li>
</ul>
