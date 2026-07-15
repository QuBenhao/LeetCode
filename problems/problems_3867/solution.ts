function gcd(a: number, b: number): number {
	while (b !== 0) {
		[a, b] = [b, a % b];
	}
	return a;
}

function gcdSum(nums: number[]): number {
	const pg = nums.map((x, i) => {
		const mx = Math.max(...nums.slice(0, i + 1));
		return gcd(x, mx);
	}).sort((a, b) => a - b);
	let i = 0, j = pg.length - 1, ans = 0;
	while (i < j) {
		ans += gcd(pg[i], pg[j]);
		i++;
		j--;
	}
	return ans;
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const nums: number[] = JSON.parse(inputValues[0]);
	return gcdSum(nums);
}
