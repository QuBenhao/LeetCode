function largestRectangleArea(heights: number[]): number {
    const stack: number[] = [-1];
	heights.push(0);
	let ans: number = 0;
	for (let i = 0; i < heights.length; i++) {
		while (stack.length > 1 && heights[i] < heights[stack[stack.length - 1]]) {
			const height: number = heights[stack.pop() as number];
			const width: number = i - stack[stack.length - 1] - 1;
			ans = Math.max(ans, height * width);
		}
		stack.push(i);
	}
	return ans;
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const heights: number[] = JSON.parse(inputValues[0]);
	return largestRectangleArea(heights);
}
