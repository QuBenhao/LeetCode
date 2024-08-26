function getImportance(employees: Employee[], id: number): number {
	const employeeMap: Map<number, Employee> = new Map();
	for (const employee of employees) {
		employeeMap.set(employee.id, employee);
	}
	const dfs = (cur: number) => {
		const e: Employee = employeeMap.get(cur)!!;
		let ans: number = e.importance;
		for (let i: number = 0; i < e.subordinates.length; i++) {
			ans += dfs(e.subordinates[i]);
		}
		return ans;
	}
	return dfs(id);
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const inputArray: any[][] = JSON.parse(inputValues[0]);
	const employees: Employee[] = new Array(inputArray.length).fill(0).map((_, i) => new Employee(inputArray[i][0], inputArray[i][1], inputArray[i][2]));
	const id: number = JSON.parse(inputValues[1]);
	return getImportance(employees, id);
}

// Definition for Employee.
class Employee {
	id: number
	importance: number
	subordinates: number[]
	constructor(id: number, importance: number, subordinates: number[]) {
		this.id = (id === undefined) ? 0 : id;
		this.importance = (importance === undefined) ? 0 : importance;
		this.subordinates = (subordinates === undefined) ? [] : subordinates;
	}
}
