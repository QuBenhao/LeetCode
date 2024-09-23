function maximumSubsequenceCount(text: string, pattern: string): number {
    
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const text: string = JSON.parse(inputValues[0]);
	const pattern: string = JSON.parse(inputValues[1]);
	return maximumSubsequenceCount(text, pattern);
}
