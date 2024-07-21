function letterCombinations(digits: string): string[] {
    
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const digits: string = JSON.parse(inputValues[0]);
	return letterCombinations(digits);
}
