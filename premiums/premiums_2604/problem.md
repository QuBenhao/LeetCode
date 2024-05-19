# 2604. Minimum Time to Eat All Grains

<p>There are <code>n</code> hens and <code>m</code> grains on a line. You are given the initial positions of the hens and the grains in two integer arrays <code>hens</code> and <code>grains</code> of size <code>n</code> and <code>m</code> respectively.</p>

<p>Any hen can eat a grain if they are on the same position. The time taken for this is negligible. One hen can also eat multiple grains.</p>

<p>In <code>1</code> second, a hen can move right or left by <code>1</code> unit. The hens can move simultaneously and independently of each other.</p>

<p>Return <em>the <strong>minimum</strong> time to eat all grains if the hens act optimally.</em></p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> hens = [3,6,7], grains = [2,4,7,9]
<strong>Output:</strong> 2
<strong>Explanation:</strong> 
One of the ways hens eat all grains in 2 seconds is described below:
- The first hen eats the grain at position 2 in 1 second. 
- The second hen eats the grain at position 4 in 2 seconds. 
- The third hen eats the grains at positions 7 and 9 in 2 seconds. 
So, the maximum time needed is 2.
It can be proven that the hens cannot eat all grains before 2 seconds.</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> hens = [4,6,109,111,213,215], grains = [5,110,214]
<strong>Output:</strong> 1
<strong>Explanation:</strong> 
One of the ways hens eat all grains in 1 second is described below:
- The first hen eats the grain at position 5 in 1 second. 
- The fourth hen eats the grain at position 110 in 1 second.
- The sixth hen eats the grain at position 214 in 1 second. 
- The other hens do not move. 
So, the maximum time needed is 1.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= hens.length, grains.length &lt;= 2*10<sup>4</sup></code></li>
	<li><code>0 &lt;= hens[i], grains[j] &lt;= 10<sup>9</sup></code></li>
</ul>
