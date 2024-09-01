function maxConsecutiveAnswers(answerKey: string, k: number): number {
	const n: number = answerKey.length;
	let ans: number = 0;
	let countT: number = 0;
	for (let left: number = 0, right: number = 0; right < n; right++) {
		if (answerKey[right] === "T") {
			countT++;
		}
		while (countT > k && right - left + 1 - countT > k) {
			if (answerKey[left] === "T") {
				countT--;
			}
			left++;
		}
		ans = Math.max(ans, right - left + 1);
	}
	return ans;
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const answerKey: string = JSON.parse(inputValues[0]);
	const k: number = JSON.parse(inputValues[1]);
	return maxConsecutiveAnswers(answerKey, k);
}
