function isAnagram(s: string, t: string): boolean {

};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const s: string = JSON.parse(inputValues[0]);
	const t: string = JSON.parse(inputValues[1]);
	return isAnagram(s, t);
}
