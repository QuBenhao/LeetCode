# 3809. Best Reachable Tower 

<p>You are given a 2D integer array <code>towers</code>, where <code>towers[i] = [x<sub>i</sub>, y<sub>i</sub>, q<sub>i</sub>]</code> represents the coordinates <code>(x<sub>i</sub>, y<sub>i</sub>)</code> and quality factor <code>q<sub>i</sub></code> of the <code>i<sup>th</sup></code> tower.</p>

<p>You are also given an integer array <code>center = [cx, cy​​​​​​​]</code> representing your location, and an integer <code>radius</code>.</p>

<p>A tower is <strong>reachable</strong> if its <strong>Manhattan distance</strong> from <code>center</code> is <strong>less than or equal</strong> to <code>radius</code>.</p>

<p>Among all reachable towers:</p>

<ul>
	<li>Return the coordinates of the tower with the <strong>maximum</strong> quality factor.</li>
	<li>If there is a tie, return the tower with the <strong>lexicographically smallest</strong> coordinate. If no tower is reachable, return <code>[-1, -1]</code>.</li>
</ul>
The <strong>Manhattan Distance</strong> between two cells <code>(x<sub>i</sub>, y<sub>i</sub>)</code> and <code>(x<sub>j</sub>, y<sub>j</sub>)</code> is <code>|x<sub>i</sub> - x<sub>j</sub>| + |y<sub>i</sub> - y<sub>j</sub>|</code>.

<p>A coordinate <code>[x<sub>i</sub>, y<sub>i</sub>]</code> is <strong>lexicographically smaller</strong> than <code>[x<sub>j</sub>, y<sub>j</sub>]</code> if <code>x<sub>i</sub> &lt; x<sub>j</sub></code>, or <code>x<sub>i</sub> == x<sub>j</sub></code> and <code>y<sub>i</sub> &lt; y<sub>j</sub></code>.</p>

<p><code>|x|</code> denotes the <strong>absolute</strong> <strong>value</strong> of <code>x</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">towers = [[1,2,5], [2,1,7], [3,1,9]], center = [1,1], radius = 2</span></p>

<p><strong>Output:</strong> <span class="example-io">[3,1]</span></p>

<p><strong>Explanation:</strong></p>

<ul>
	<li>Tower <code>[1, 2, 5]</code>: Manhattan distance = <code>|1 - 1| + |2 - 1| = 1</code>, reachable.</li>
	<li>Tower <code>[2, 1, 7]</code>: Manhattan distance = <code>|2 - 1| + |1 - 1| = 1</code>, reachable.</li>
	<li>Tower <code>[3, 1, 9]</code>: Manhattan distance = <code>|3 - 1| + |1 - 1| = 2</code>, reachable.</li>
</ul>

<p>All towers are reachable. The maximum quality factor is 9, which corresponds to tower <code>[3, 1]</code>.</p>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">towers = [[1,3,4], [2,2,4], [4,4,7]], center = [0,0], radius = 5</span></p>

<p><strong>Output:</strong> <span class="example-io">[1,3]</span></p>

<p><strong>Explanation:</strong></p>

<ul>
	<li>Tower <code>[1, 3, 4]</code>: Manhattan distance = <code>|1 - 0| + |3 - 0| = 4</code>, reachable.</li>
	<li>Tower <code>[2, 2, 4]</code>: Manhattan distance = <code>|2 - 0| + |2 - 0| = 4</code>, reachable.</li>
	<li>Tower <code>[4, 4, 7]</code>: Manhattan distance = <code>|4 - 0| + |4 - 0| = 8</code>, not reachable.</li>
</ul>

<p>Among the reachable towers, the maximum quality factor is 4. Both <code>[1, 3]</code> and <code>[2, 2]</code> have the same quality, so the lexicographically smaller coordinate is <code>[1, 3]</code>.</p>
</div>

<p><strong class="example">Example 3:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">towers = [[5,6,8], [0,3,5]], center = [1,2], radius = 1</span></p>

<p><strong>Output:</strong> <span class="example-io">[-1,-1]</span></p>

<p><strong>Explanation:</strong></p>

<ul>
	<li>Tower <code>[5, 6, 8]</code>: Manhattan distance = <code>|5 - 1| + |6 - 2| = 8</code>, not reachable.</li>
	<li>Tower <code>[0, 3, 5]</code>: Manhattan distance = <code>|0 - 1| + |3 - 2| = 2</code>, not reachable.</li>
</ul>

<p>No tower is reachable within the given radius, so <code>[-1, -1]</code> is returned.</p>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= towers.length &lt;= 10<sup>5</sup></code></li>
	<li><code>towers[i] = [x<sub>i</sub>, y<sub>i</sub>, q<sub>i</sub>]</code></li>
	<li><code>center = [cx, cy]</code></li>
	<li><code>0 &lt;= x<sub>i</sub>, y<sub>i</sub>, q<sub>i</sub>, cx, cy &lt;= 10<sup>5</sup></code>​​​​​​​</li>
	<li><code>0 &lt;= radius &lt;= 10<sup>5</sup></code></li>
</ul>
