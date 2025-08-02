function maxTotalFruits(fruits: number[][], startPos: number, k: number): number {
    
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const fruits: number[][] = JSON.parse(inputValues[0]);
	const startPos: number = JSON.parse(inputValues[1]);
	const k: number = JSON.parse(inputValues[2]);
	return maxTotalFruits(fruits, startPos, k);
}
