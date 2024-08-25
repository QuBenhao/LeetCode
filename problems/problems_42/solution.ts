function trap(height: number[]): number {
	const n: number = height.length;
	const rightMax: number[] = new Array(n).fill(0);
	for (let i: number = n - 2; i >= 0; i--) {
		rightMax[i] = Math.max(rightMax[i + 1], height[i + 1]);
	}
	let leftMax: number = 0, ans: number = 0;
	for (let i: number = 1; i < n - 1; i++) {
		leftMax = Math.max(leftMax, height[i - 1]);
		const min: number = Math.min(leftMax, rightMax[i]);
		if (min > height[i]) {
			ans += min - height[i];
		}
	}
	return ans;
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const height: number[] = JSON.parse(inputValues[0]);
	return trap(height);
}
