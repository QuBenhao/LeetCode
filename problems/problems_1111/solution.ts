function maxDepthAfterSplit(seq: string): number[] {
    
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const seq: string = JSON.parse(inputValues[0]);
	return maxDepthAfterSplit(seq);
}
