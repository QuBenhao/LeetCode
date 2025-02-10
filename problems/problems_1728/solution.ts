function canMouseWin(grid: string[], catJump: number, mouseJump: number): boolean {
    
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const grid: string[] = JSON.parse(inputValues[0]);
	const catJump: number = JSON.parse(inputValues[1]);
	const mouseJump: number = JSON.parse(inputValues[2]);
	return canMouseWin(grid, catJump, mouseJump);
}
