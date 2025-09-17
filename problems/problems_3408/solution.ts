class TaskManager {
    constructor(tasks: number[][]) {
        
    }

    add(userId: number, taskId: number, priority: number): void {
        
    }

    edit(taskId: number, newPriority: number): void {
        
    }

    rmv(taskId: number): void {
        
    }

    execTop(): number {
        
    }
}

/**
 * Your TaskManager object will be instantiated and called as such:
 * var obj = new TaskManager(tasks)
 * obj.add(userId,taskId,priority)
 * obj.edit(taskId,newPriority)
 * obj.rmv(taskId)
 * var param_4 = obj.execTop()
 */

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const operators: string[] = JSON.parse(inputValues[0]);
	const opValues: any[][] = JSON.parse(inputValues[1]);
	const ans: any[] = [null];
	const obj: TaskManager = new TaskManager(opValues[0][0]);
	for (let i: number = 1; i < operators.length; i++) {
		if (operators[i] == "add") {
			obj.add(opValues[i][0], opValues[i][1], opValues[i][2]);
			ans.push(null);
			continue;
		}
		if (operators[i] == "edit") {
			obj.edit(opValues[i][0], opValues[i][1]);
			ans.push(null);
			continue;
		}
		if (operators[i] == "rmv") {
			obj.rmv(opValues[i][0]);
			ans.push(null);
			continue;
		}
		if (operators[i] == "execTop") {
			ans.push(obj.execTop());
			continue;
		}
		ans.push(null);
	}
	return ans;
}
