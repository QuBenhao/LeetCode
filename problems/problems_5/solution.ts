/**
 * @param {string} s
 * @return {string}
 */
var longestPalindrome = function (s) {
  let max = 0 // Length of the longest palindrome found so far
  let start = -1 // Starting index of the longest palindrome found so far
  const len = s.length // Length of s
  for (let i = 0; i < len; i++) { // Traverse s
    let now = 1 // Length of the current palindrome
    let l = i - 1 // Pointer to start scanning on the left
    while (s[i + 1] === s[i]) { // While following characters match the current one, add 1 to the length and advance the pointer in s
      now++
      i++
    }
    let r = i + 1 // Get the pointer to start scanning on the right
    while (s[l] === s[r] && s[l] !== undefined) {  // Expand outward from the run of equal characters until out of bounds or a mismatch; add matches to the current length and move both pointers
      now += 2
      l--
      r++
    }
    if (now > max) { // Compare with the previous maximum and update the starting index of the longest palindrome
      max = now
      start = l + 1
    }
  }
  return s.slice(start, start + max) // Extract the required string using the maximum length and starting index
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const s: string = JSON.parse(inputValues[0]);
	return longestPalindrome(s);
}
