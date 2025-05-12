function lengthAfterTransformations(s: string, t: number): number {
    
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const s: string = JSON.parse(inputValues[0]);
	const t: number = JSON.parse(inputValues[1]);
	return lengthAfterTransformations(s, t);
}
