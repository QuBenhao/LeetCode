function maxArea(height: number[]): number {
    let ans: number = 0;
	for (let left: number = 0, right: number = height.length - 1; left < right; ) {
		ans = Math.max(ans, Math.min(height[left], height[right]) * (right - left));
		if (height[left] < height[right]) {
			left++;
		} else {
			right--;
		}
	}
	return ans;
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const height: number[] = JSON.parse(inputValues[0]);
	return maxArea(height);
}
