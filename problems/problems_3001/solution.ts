function minMovesToCaptureTheQueen(a: number, b: number, c: number, d: number, e: number, f: number): number {
    
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const a: number = JSON.parse(inputValues[0]);
	const b: number = JSON.parse(inputValues[1]);
	const c: number = JSON.parse(inputValues[2]);
	const d: number = JSON.parse(inputValues[3]);
	const e: number = JSON.parse(inputValues[4]);
	const f: number = JSON.parse(inputValues[5]);
	return minMovesToCaptureTheQueen(a, b, c, d, e, f);
}
