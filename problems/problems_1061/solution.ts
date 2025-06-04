function smallestEquivalentString(s1: string, s2: string, baseStr: string): string {
    
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const s1: string = JSON.parse(inputValues[0]);
	const s2: string = JSON.parse(inputValues[1]);
	const baseStr: string = JSON.parse(inputValues[2]);
	return smallestEquivalentString(s1, s2, baseStr);
}
