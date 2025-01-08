function validSubstringCount(word1: string, word2: string): number {
    
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const word1: string = JSON.parse(inputValues[0]);
	const word2: string = JSON.parse(inputValues[1]);
	return validSubstringCount(word1, word2);
}
