# 2868. The Wording Game

<p>Alice and Bob each have a <strong>lexicographically sorted</strong> array of strings named <code>a</code> and <code>b</code> respectively.</p>

<p>They are playing a wording game with the following rules:</p>

<ul>
	<li>On each turn, the current player should play a word from their list such that the new word is <strong>closely greater</strong> than the last played word; then it&#39;s the other player&#39;s turn.</li>
	<li>If a player can&#39;t play a word on their turn, they lose.</li>
</ul>

<p>Alice starts the game by playing her <strong>lexicographically </strong><strong>smallest </strong>word.</p>

<p>Given <code>a</code> and <code>b</code>, return <code>true</code> <em>if Alice can win knowing that both players play their best, and</em> <code>false</code> <em>otherwise.</em></p>

<p>A word <code>w</code> is <strong>closely greater</strong> than a word <code>z</code> if the following conditions are met:</p>

<ul>
	<li><code>w</code> is <strong>lexicographically greater</strong> than <code>z</code>.</li>
	<li>If <code>w<sub>1</sub></code> is the first letter of <code>w</code> and <code>z<sub>1</sub></code> is the first letter of <code>z</code>, <code>w<sub>1</sub></code> should either be <strong>equal</strong> to <code>z<sub>1</sub></code> or be the <strong>letter after</strong> <code>z<sub>1</sub></code> in the alphabet.</li>
	<li>For example, the word <code>&quot;care&quot;</code> is closely greater than <code>&quot;book&quot;</code> and <code>&quot;car&quot;</code>, but is not closely greater than <code>&quot;ant&quot;</code> or <code>&quot;cook&quot;</code>.</li>
</ul>

<p>A string <code>s</code> is <b>lexicographically </b><strong>greater</strong> than a string <code>t</code> if in the first position where <code>s</code> and <code>t</code> differ, string <code>s</code> has a letter that appears later in the alphabet than the corresponding letter in <code>t</code>. If the first <code>min(s.length, t.length)</code> characters do not differ, then the longer string is the lexicographically greater one.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> a = [&quot;avokado&quot;,&quot;dabar&quot;], b = [&quot;brazil&quot;]
<strong>Output:</strong> false
<strong>Explanation:</strong> Alice must start the game by playing the word &quot;avokado&quot; since it&#39;s her smallest word, then Bob plays his only word, &quot;brazil&quot;, which he can play because its first letter, &#39;b&#39;, is the letter after Alice&#39;s word&#39;s first letter, &#39;a&#39;.
Alice can&#39;t play a word since the first letter of the only word left is not equal to &#39;b&#39; or the letter after &#39;b&#39;, &#39;c&#39;.
So, Alice loses, and the game ends.</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> a = [&quot;ananas&quot;,&quot;atlas&quot;,&quot;banana&quot;], b = [&quot;albatros&quot;,&quot;cikla&quot;,&quot;nogomet&quot;]
<strong>Output:</strong> true
<strong>Explanation:</strong> Alice must start the game by playing the word &quot;ananas&quot;.
Bob can&#39;t play a word since the only word he has that starts with the letter &#39;a&#39; or &#39;b&#39; is &quot;albatros&quot;, which is smaller than Alice&#39;s word.
So Alice wins, and the game ends.</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> a = [&quot;hrvatska&quot;,&quot;zastava&quot;], b = [&quot;bijeli&quot;,&quot;galeb&quot;]
<strong>Output:</strong> true
<strong>Explanation:</strong> Alice must start the game by playing the word &quot;hrvatska&quot;.
Bob can&#39;t play a word since the first letter of both of his words are smaller than the first letter of Alice&#39;s word, &#39;h&#39;.
So Alice wins, and the game ends.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= a.length, b.length &lt;= 10<sup>5</sup></code></li>
	<li><code>a[i]</code> and <code>b[i]</code> consist only of lowercase English letters.</li>
	<li><code>a</code> and <code>b</code> are <strong>lexicographically sorted</strong>.</li>
	<li>All the words in <code>a</code> and <code>b</code> combined are <strong>distinct</strong>.</li>
	<li>The sum of the lengths of all the words in <code>a</code> and <code>b</code> combined does not exceed <code>10<sup>6</sup></code>.</li>
</ul>
