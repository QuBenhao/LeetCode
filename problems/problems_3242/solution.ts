class NeighborSum {
    constructor(grid: number[][]) {
        
    }

    adjacentSum(value: number): number {
        
    }

    diagonalSum(value: number): number {
        
    }
}

/**
 * Your NeighborSum object will be instantiated and called as such:
 * var obj = new NeighborSum(grid)
 * var param_1 = obj.adjacentSum(value)
 * var param_2 = obj.diagonalSum(value)
 */

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const operators: string[] = JSON.parse(inputValues[0]);
	const opValues: any[][] = JSON.parse(inputValues[1]);
	const ans: any[] = [null];
	const obj: NeighborSum = new NeighborSum(opValues[0][0]);
	for (let i: number = 1; i < operators.length; i++) {
		if (operators[i] == "adjacentSum") {
			ans.push(obj.adjacentSum(opValues[i][0]));
			continue;
		}
		if (operators[i] == "diagonalSum") {
			ans.push(obj.diagonalSum(opValues[i][0]));
			continue;
		}
		ans.push(null);
	}
	return ans;
}
