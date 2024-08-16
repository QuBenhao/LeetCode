function checkInclusion(s1: string, s2: string): boolean {

};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const s1: string = JSON.parse(inputValues[0]);
	const s2: string = JSON.parse(inputValues[1]);
	return checkInclusion(s1, s2);
}
