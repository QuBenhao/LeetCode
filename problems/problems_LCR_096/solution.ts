function isInterleave(s1: string, s2: string, s3: string): boolean {

};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const s1: string = JSON.parse(inputValues[0]);
	const s2: string = JSON.parse(inputValues[1]);
	const s3: string = JSON.parse(inputValues[2]);
	return isInterleave(s1, s2, s3);
}
