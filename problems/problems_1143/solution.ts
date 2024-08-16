function longestCommonSubsequence(text1: string, text2: string): number {
    
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const text1: string = JSON.parse(inputValues[0]);
	const text2: string = JSON.parse(inputValues[1]);
	return longestCommonSubsequence(text1, text2);
}
