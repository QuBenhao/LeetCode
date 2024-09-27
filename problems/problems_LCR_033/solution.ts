function groupAnagrams(strs: string[]): string[][] {

};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const strs: string[] = JSON.parse(inputValues[0]);
	return groupAnagrams(strs);
}
