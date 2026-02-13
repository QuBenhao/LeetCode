function champagneTower(poured: number, query_row: number, query_glass: number): number {
    
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const poured: number = JSON.parse(inputValues[0]);
	const query_row: number = JSON.parse(inputValues[1]);
	const query_glass: number = JSON.parse(inputValues[2]);
	return champagneTower(poured, query_row, query_glass);
}
