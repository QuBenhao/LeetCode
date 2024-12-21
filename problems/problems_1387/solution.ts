function getKth(lo: number, hi: number, k: number): number {
    
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const lo: number = JSON.parse(inputValues[0]);
	const hi: number = JSON.parse(inputValues[1]);
	const k: number = JSON.parse(inputValues[2]);
	return getKth(lo, hi, k);
}
