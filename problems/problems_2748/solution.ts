function gcd(a: number, b: number): number {
	return b == 0 ? a : gcd(b, a % b);
}

function countBeautifulPairs(nums: number[]): number {
	let ans: number = 0;
	const counter: Array<number> = new Array<number>(10).fill(0);
	for (let num of nums) {
		const cur: number = num % 10;
		for (let i: number = 1; i < counter.length; i++) {
			if (counter[i] > 0 && gcd(cur, i) == 1) {
				ans += counter[i];
			}
		}
		while (num >= 10) {
			num = Math.floor(num / 10);
		}
		counter[num]++;
	}
	return ans;
};

export function Solve(inputJsonElement: string): any {
	const splits: string[] = inputJsonElement.split("\n");
	const nums: number[] = JSON.parse(splits[0]);
	return countBeautifulPairs(nums);
}
