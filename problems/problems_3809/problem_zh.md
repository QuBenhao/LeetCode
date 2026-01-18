# 3809. 最好可到达的塔 

<p>给你一个二维整数数组 <code>towers</code>，其中 <code>towers[i] = [x<sub>i</sub>, y<sub>i</sub>, q<sub>i</sub>]</code> 表示第 <code>i</code> 座塔的坐标 <code>(x<sub>i</sub>, y<sub>i</sub>)</code> 和质量因子 <code>q<sub>i</sub></code>。</p>

<p>另外给你一个整数数组 <code>center = [cx, cy]</code> 表示你的位置，以及一个整数 <code>radius</code>。</p>

<p>如果一座塔与 <code>center</code> 之间的 <strong>曼哈顿距离</strong><strong>小于或等于</strong> <code>radius</code>，则称该塔是 <strong>可到达的</strong>。</p>

<p>在所有可到达的塔中：</p>

<ul>
	<li>返回质量因子 <strong>最大</strong> 的塔的坐标。</li>
	<li>如果存在并列的塔，返回坐标 <strong>字典序最小</strong> 的塔。如果没有塔是可到达的，返回 <code>[-1, -1]</code>。</li>
</ul>
两点 <code>(x<sub>i</sub>, y<sub>i</sub>)</code> 和 <code>(x<sub>j</sub>, y<sub>j</sub>)</code> 之间的 <strong>曼哈顿距离</strong> 为 <code>|x<sub>i</sub> - x<sub>j</sub>| + |y<sub>i</sub> - y<sub>j</sub>|</code>。

<p>坐标 <code>[x<sub>i</sub>, y<sub>i</sub>]</code> <strong>字典序小于</strong> <code>[x<sub>j</sub>, y<sub>j</sub>]</code> 是指：<code>x<sub>i</sub> &lt; x<sub>j</sub></code>，或者 <code>x<sub>i</sub> == x<sub>j</sub></code> 且 <code>y<sub>i</sub> &lt; y<sub>j</sub></code>。</p>

<p><code>|x|</code> 表示 <code>x</code> 的 <strong>绝对值</strong>。</p>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>

<div class="example-block">
<p><strong>输入：</strong> <span class="example-io">towers = [[1,2,5], [2,1,7], [3,1,9]], center = [1,1], radius = 2</span></p>

<p><strong>输出：</strong> <span class="example-io">[3,1]</span></p>

<p><strong>解释：</strong></p>

<ul>
	<li>塔 <code>[1, 2, 5]</code>：曼哈顿距离 = <code>|1 - 1| + |2 - 1| = 1</code>，可到达。</li>
	<li>塔 <code>[2, 1, 7]</code>：曼哈顿距离 = <code>|2 - 1| + |1 - 1| = 1</code>，可到达。</li>
	<li>塔 <code>[3, 1, 9]</code>：曼哈顿距离 = <code>|3 - 1| + |1 - 1| = 2</code>，可到达。</li>
</ul>

<p>所有塔都是可到达的。最大质量因子为 9，对应塔 <code>[3, 1]</code>。</p>
</div>

<p><strong class="example">示例 2：</strong></p>

<div class="example-block">
<p><strong>输入：</strong> <span class="example-io">towers = [[1,3,4], [2,2,4], [4,4,7]], center = [0,0], radius = 5</span></p>

<p><strong>输出：</strong> <span class="example-io">[1,3]</span></p>

<p><strong>解释：</strong></p>

<ul>
	<li>塔 <code>[1, 3, 4]</code>：曼哈顿距离 = <code>|1 - 0| + |3 - 0| = 4</code>，可到达。</li>
	<li>塔 <code>[2, 2, 4]</code>：曼哈顿距离 = <code>|2 - 0| + |2 - 0| = 4</code>，可到达。</li>
	<li>塔 <code>[4, 4, 7]</code>：曼哈顿距离 = <code>|4 - 0| + |4 - 0| = 8</code>，不可到达。</li>
</ul>

<p>在可到达的塔中，最大质量因子为 4。<code>[1, 3]</code> 和 <code>[2, 2]</code> 的质量因子相同，因此返回字典序较小的坐标 <code>[1, 3]</code>。</p>
</div>

<p><strong class="example">示例 3：</strong></p>

<div class="example-block">
<p><strong>输入：</strong> <span class="example-io">towers = [[5,6,8], [0,3,5]], center = [1,2], radius = 1</span></p>

<p><strong>输出：</strong> <span class="example-io">[-1,-1]</span></p>

<p><strong>解释：</strong></p>

<ul>
	<li>塔 <code>[5, 6, 8]</code>：曼哈顿距离 = <code>|5 - 1| + |6 - 2| = 8</code>，不可到达。</li>
	<li>塔 <code>[0, 3, 5]</code>：曼哈顿距离 = <code>|0 - 1| + |3 - 2| = 2</code>，不可到达。</li>
</ul>

<p>在给定半径内没有可到达的塔，故返回 <code>[-1, -1]</code>。</p>
</div>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= towers.length &lt;= 10<sup>5</sup></code></li>
	<li><code>towers[i] = [x<sub>i</sub>, y<sub>i</sub>, q<sub>i</sub>]</code></li>
	<li><code>center = [cx, cy]</code></li>
	<li><code>0 &lt;= x<sub>i</sub>, y<sub>i</sub>, q<sub>i</sub>, cx, cy &lt;= 10<sup>5</sup></code></li>
	<li><code>0 &lt;= radius &lt;= 10<sup>5</sup></code></li>
</ul>
