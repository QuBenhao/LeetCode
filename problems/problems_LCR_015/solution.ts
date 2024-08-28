function findAnagrams(s: string, p: string): number[] {

};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const s: string = JSON.parse(inputValues[0]);
	const p: string = JSON.parse(inputValues[1]);
	return findAnagrams(s, p);
}
