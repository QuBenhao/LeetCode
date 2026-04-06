class Robot {
    constructor(width: number, height: number) {
        
    }

    step(num: number): void {
        
    }

    getPos(): number[] {
        
    }

    getDir(): string {
        
    }
}

/**
 * Your Robot object will be instantiated and called as such:
 * var obj = new Robot(width, height)
 * obj.step(num)
 * var param_2 = obj.getPos()
 * var param_3 = obj.getDir()
 */

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const operators: string[] = JSON.parse(inputValues[0]);
	const opValues: any[][] = JSON.parse(inputValues[1]);
	const ans: any[] = [null];
	const obj: Robot = new Robot(opValues[0][0], opValues[0][1]);
	for (let i: number = 1; i < operators.length; i++) {
		if (operators[i] == "step") {
			obj.step(opValues[i][0]);
			ans.push(null);
			continue;
		}
		if (operators[i] == "getPos") {
			ans.push(obj.getPos());
			continue;
		}
		if (operators[i] == "getDir") {
			ans.push(obj.getDir());
			continue;
		}
		ans.push(null);
	}
	return ans;
}
