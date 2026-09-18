function checkOverlap(radius: number, xCenter: number, yCenter: number, x1: number, y1: number, x2: number, y2: number): boolean {
    
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const radius: number = JSON.parse(inputValues[0]);
	const xCenter: number = JSON.parse(inputValues[1]);
	const yCenter: number = JSON.parse(inputValues[2]);
	const x1: number = JSON.parse(inputValues[3]);
	const y1: number = JSON.parse(inputValues[4]);
	const x2: number = JSON.parse(inputValues[5]);
	const y2: number = JSON.parse(inputValues[6]);
	return checkOverlap(radius, xCenter, yCenter, x1, y1, x2, y2);
}
